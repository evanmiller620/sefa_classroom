import shutil
import os

def putGradesInRepos(rootDirGrades, fileName, userList, hwName):
	for user in userList:
		owd = os.getcwd()
		srcPath = str(owd + rootDirGrades + "/" + hwName + "-" + user + "/" + fileName)
		dstPath = str(owd + "/clones/" + hwName + "-" + user)
		if os.path.exists(str(srcPath)) and os.path.exists(str(dstPath)):
			shutil.copy(srcPath, dstPath)
		else:
			print("One of these directories does not exist: " +  str(srcPath) + " or " + str(dstPath))