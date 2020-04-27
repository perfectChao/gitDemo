#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

# podspec name
module = sys.argv[1]
# git tag
tag = sys.argv[2]
# commit message
message = sys.argv[3]

############ 配置 ##############
repo_name = 'gitee_specs'
repo_source = 'https://gitee.com/perfectChao/PrivatePodspec.git'


# 提交代码
def git_commit():
	os.system('git add .')
	os.system('git commit -m"{}"'.format(message))
	res = os.system('git push origin master')
	if res == 0:
		print('推送远程仓库成功 ----- ✅ ')
	else:
		print('推送远程仓库失败 ----- ❌ ')
		exit()

# 更新tag
def git_update_tag():
	print('🍰 更新tag')
	if os.system('git rev-parse -q --verify "refs/tags/{}"'.format(tag)) == 0:
		print('tag 存在 ----- ❗️')
		git_delete_tag()
		git_add_tag()
	else:
		print('tag 不存在 ----- ❗️')
		git_add_tag()

# 删除tag
def git_delete_tag():
	os.system('git tag -d ' + tag)
	if os.system('git push origin :refs/tags/' + tag) == 0:
		print('删除远端tag成功 ----- ✅ ')
	else:
		print('删除远端tag失败 ----- ❌')
		exit()

# 添加tag
def git_add_tag():
	os.system('git tag ' + tag)
	if os.system('git push origin --tags') == 0:
		print('新建远端tag成功 ----- ✅')
	else:
		print('新建远端tag失败 ----- ❌')
		exit()

def git_repo_push():
	print('🍰🍰🍰 推送spec文件...')
	os.system('pod cache clean ' + module + ' --all')
	repo_cmd = 'pod repo push {} '.format(repo_name)
	repo_cmd += (module + '.podspec')
	repo_cmd += ' --sources={}'.format(repo_source)
	repo_cmd += ' --allow-warnings --verbose --use-libraries'
	if os.system(repo_cmd) == 0:
		print('推送{},{}成功 ----- ✅'.format(module, tag))
	else:
		print('推送{},{}失败 ----- ❌'.format(module, tag))


git_commit()
git_update_tag()
git_repo_push()



