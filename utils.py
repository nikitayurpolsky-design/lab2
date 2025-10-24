def format_timestamp():
    """Возвращает текущую метку времени для документации"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_project_info():
    """Возвращает информацию о проекте"""
    return {
        "name": "CI/CD Lab Project",
        "version": "1.1.0",
        "last_updated": format_timestamp()
    }