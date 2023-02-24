def retrieve_major(semver):
	semver = semver.split(".")
	return str(semver[0])

def retrieve_minor(semver):
	semver = semver.split(".")
	return str(semver[1])

def retrieve_patch(semver):
	semver = semver.split(".")
	return str(semver[2])