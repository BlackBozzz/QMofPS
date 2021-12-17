from Functions import *
import os
import pytest


@pytest.fixture()
def PreCreateNewFolder():
    CreateNewFolder("ABC")
    return os.path.getsize("ABC")

def test_CreateNewFolder(PreCreateNewFolder):
    assert PreCreateNewFolder != 0

#Нет прав на удаление
"""@pytest.fixture() 
def PreDeleteFolder():
    DeleteFolder("ABC")
    return "ABC"

def test_DeleteFolder(PreDeleteFolder):
    assert PreDeleteFolder != 0"""

def test_FolderLevelUp():
    assert FolderLevelUp()


@pytest.fixture()
def PreCheckPath():
    CheckPath("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/123")
    return os.path.getsize("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/123")

def test_CheckPath(PreCheckPath):
    assert PreCheckPath != 0


@pytest.fixture()
def PreMoveToFolder():
    MoveToFolder("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/123")
    return os.path.getsize("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/123")

def test_MoveToFolder(PreMoveToFolder):
    assert PreMoveToFolder != 0


@pytest.fixture()
def PreCreateNewFile():
    CreateNewFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/1.txt")
    return True

def test_CreateNewFile(PreCreateNewFile):
    assert PreCreateNewFile != 0


@pytest.fixture()
def PreWriteInFile():
    WriteInFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/1.txt", "345678909876")
    return os.path.getsize("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/1.txt")

def test_WriteInFile(PreWriteInFile):
    assert PreWriteInFile != 0


@pytest.fixture()
def PreShowFile():
    ShowFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/1.txt")
    return os.path.getsize("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/1.txt")

def test_ShowFile(PreShowFile):
    assert PreShowFile != 0


@pytest.fixture()
def PreCopyFile():
    CopyFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/1.txt", "/Users/georgijgusakov/PycharmProjects/TestManager/Admin/2.txt")
    return os.path.getsize("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/2.txt")

def test_CopyFile(PreCopyFile):
    assert PreCopyFile != 0

@pytest.fixture()
def PreMoveFile():
    MoveFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/1.txt", "/Users/georgijgusakov/PycharmProjects/TestManager/Admin/ABC")
    return os.path.getsize("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/ABC/1.txt")

def test_MoveFile(PreMoveFile):
    assert PreMoveFile != 0

@pytest.fixture()
def PreRenameFile():
    RenameFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/1.txt", "/Users/georgijgusakov/PycharmProjects/TestManager/Admin/ABC")
    return os.path.getsize("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/ABC/1.txt")

def test_RenameFile(PreRenameFile):
    assert PreRenameFile != 0


@pytest.fixture()
def negative_PreCreateNewFolder():
    CreateNewFolder("")
    return True

@pytest.mark.xfail()
def test_negative_CreateNewFolder(negative_PreCreateNewFolder):
    assert negative_PreCreateNewFolder

@pytest.fixture()
def negative_PreDeleteFolder():
    DeleteFolder("ABC")
    return "ABC"

@pytest.mark.xfail()
def test_negative_DeleteFolder(negative_PreDeleteFolder):
    assert negative_PreDeleteFolder

@pytest.mark.xfail()
def test_negative_FolderLevelUp():
    assert FolderLevelUp()


@pytest.fixture()
def negative_PreCheckPath():
    CheckPath("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/12")
    return True

@pytest.mark.xfail()
def test_negative_CheckPath(negative_PreCheckPath):
    assert negative_PreCheckPath != 0


@pytest.fixture()
def negative_PreMoveToFolder():
    MoveToFolder("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/122")
    return True

@pytest.mark.xfail()
def test_negative_MoveToFolder(negative_PreMoveToFolder):
    assert negative_PreMoveToFolder != 0


@pytest.fixture()
def negative_PreCreateNewFile():
    CreateNewFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/.txt")
    return True

@pytest.mark.xfail()
def negative_test_CreateNewFile(negative_PreCreateNewFile):
    assert negative_PreCreateNewFile != 0


@pytest.fixture()
def negative_PreWriteInFile():
    WriteInFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/.txt", "345678909876")
    return True

@pytest.mark.xfail()
def test_negative_WriteInFile(negative_PreWriteInFile):
    assert negative_PreWriteInFile != 0


@pytest.fixture()
def negative_PreShowFile():
    ShowFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/.txt")
    return True

@pytest.mark.xfail()
def test_negative_ShowFile(negative_PreShowFile):
    assert negative_PreShowFile != 0


@pytest.fixture()
def negative_PreCopyFile():
    CopyFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/.txt", "/Users/georgijgusakov/PycharmProjects/TestManager/Admin/.txt")
    return True

@pytest.mark.xfail()
def test_negative_CopyFile(negative_PreCopyFile):
    assert negative_PreCopyFile != 0

@pytest.fixture()
def negative_PreMoveFile():
    MoveFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/.txt", "/Users/georgijgusakov/PycharmProjects/TestManager/Admin/ABC")
    return True

@pytest.mark.xfail()
def test_negative_MoveFile(negative_PreMoveFile):
    assert negative_PreMoveFile != 0

@pytest.fixture()
def negative_PreRenameFile():
    RenameFile("/Users/georgijgusakov/PycharmProjects/TestManager/Admin/.txt", "/Users/georgijgusakov/PycharmProjects/TestManager/Admin/ABC")
    return True

@pytest.mark.xfail()
def test_negative_RenameFile(negative_PreRenameFile):
    assert negative_PreRenameFile != 0