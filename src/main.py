'''
 ______  ____  ______  _        ___ 
|      Tl    j|      T| T      /  _]
|      | |  T |      || |     /  [_ 
l_j  l_j |  | l_j  l_j| l___ Y    _]
  |  |   |  |   |  |  |     T|   [_ 
  |  |   j  l   |  |  |     ||     T
  l__j  |____j  l__j  l_____jl_____j
'''

from preloads import *

'''
 _       __    _   _     
| |\/|  / /\  | | | |\ | 
|_|  | /_/--\ |_| |_| \|
'''

def main():
    while True:
        url = input('Insert YouTube video: ')

        if 'youtube.com/watch?v=' not in url:
            print ('Only youtube videos.')
            continue

        else:
            break
        
    vid_creator_mongo(url)       

if __name__ == '__main__':
    main()