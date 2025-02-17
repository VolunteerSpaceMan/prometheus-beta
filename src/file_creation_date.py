import os
import platform
import datetime

def get_file_creation_date(file_path):
    """
    Get the creation date of a file across different platforms.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        datetime: Creation date and time of the file
    
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If there's no permission to access file metadata
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        system = platform.system()
        
        if system == 'Windows':
            # Windows uses file creation time directly
            creation_time = os.path.getctime(file_path)
            return datetime.datetime.fromtimestamp(creation_time)
        
        elif system == 'Darwin':  # macOS
            # macOS stores creation time differently
            stat_info = os.stat(file_path)
            # Use st_birthtime for macOS
            creation_time = getattr(stat_info, 'st_birthtime', stat_info.st_mtime)
            return datetime.datetime.fromtimestamp(creation_time)
        
        else:  # Linux and other Unix-like systems
            # Linux typically uses metadata change time as the closest approximation
            stat_info = os.stat(file_path)
            return datetime.datetime.fromtimestamp(stat_info.st_ctime)
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file metadata for: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error retrieving file creation date: {str(e)}")