# 디렉터리란?
# 파일은 어떤 디렉터리 directory 에 있습니다.

# 디렉터리는 파일을 분류하기 위해 사용하는 공간 입니다.
# 윈도우 운영체제에서는 폴더 folder 라고 부릅니다.
# 디렉터리와 폴더의 정확한 개념은 다릅니다. 하지만 파일을 모아놓는 곳이라는 점에서 비슷합니다.
# 디렉터리 또는 디렉토리라고 합니다.
# 현재 작업중인(위치한) 디렉터리를 작업 디렉터리 working directory 라고 합니다.

# 현재 작업중인 디렉터리의 위치를 찾아봅시다.

# pwd : print working directory 의 약자, 현재 위치를 출력해주는 명령어 입니다.
# [ ]
# pwd

# 새로운 디렉터리를 만들어 봅시다.
# mkdir : make directory 의 약자, 현재 작업 디렉터리에서 새로운 디렉터리를 만듭니다.
# [ ]
# mkdir test
# 새로 만든 디렉터리로 이동해 봅시다.
# cd : change directory 의 약자, 현재 작업 디렉터리에서 새로운 디렉터리로 이동합니다.
# [ ]
# cd test
# /content/test
# 현재 작업 디렉터리의 위치를 확인해 봅시다.
# [ ]
# pwd

# 경로명은 현재 파일이 어떤 디렉터리에 있는지 알려줍니다.

# 디렉터리는 트리 tree 구조로 구성되어 있습니다.

# 트리 구조는 최상단에 루트 root (/ 로 표시)를 시작으로, 마치 나무 가지가 뻗어나가듯이 구성되는 구조를 말합니다.
# 루트, 즉 뿌리가 최상단에 있으므로, 나무가 거꾸로 있다고 상상해 보세요.
# 루트를 시작으로 디렉터리, 그 안에 디렉터리, 또 그 안에 디렉터리가 있고 가장 끝에 파일이 있습니다.
# 경로명이 /content/test 라면,

# 루트(/) > content > test 순으로 디렉터리가 있습니다.
# 루트부터 경로명을 표시하는 방법을 절대 경로라고 합니다.

# 현재 위치를 기준으로 표시하는 방법을 상대 경로라고 합니다.

# 상대 경로에서 현재 위치는 ./ 로 표시합니다.
# 현재 위치를 기준으로 상위 디렉터리는 ../ 로 표시합니다.
# [ ]
# cd ..
# /content