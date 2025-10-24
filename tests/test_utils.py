from utils import get_project_info

def test_get_project_info():
    """Тест функции получения информации о проекте"""
    info = get_project_info()
    assert "name" in info
    assert "version" in info
    assert "last_updated" in info
    assert info["name"] == "CI/CD Lab Project"