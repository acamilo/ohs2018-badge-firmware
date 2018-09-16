from github import Github,GithubException
import subprocess
import os

                   
token = os.environ['GH_TOKEN']
token = token.strip()
git = Github(token)

org = git.get_organization('oshwabadge2018')
repo = org.get_repo('ohs2018-badge-firmware')


tag = os.environ['TRAVIS_TAG']
name = "Release %s" % tag
message = ""
 
release = repo.create_git_release(tag,name,message)
release.upload_asset("micropython/ports/esp32/build/firmware.bin")

r = repo.get_latest_release()

download_url = None
for a in r.get_assets():
  if a.name=='firmware.bin':
    download_url = a.browser_download_url

md5 = subprocess.check_output(["md5sum", "micropython/ports/esp32/build/firmware.bin"]).split(" ")[0]
json = "{\"version\":\"%s\",\"md5\":\"%s\",\"download\":\"%s\"}" % \
  (tag,md5,download_url)

print json

vfile = open('fwd.json','w+')
vfile.write(json)
vfile.close()



