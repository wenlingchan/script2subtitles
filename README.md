# script2subtitles
Auto insert line breaks to a Chinese script to form lines of subtitles

## Example
Input:
```
人生幾何，夕陽幾度。不經意間的一次擦肩而過，都會成為我們記憶中最靚麗的一道風景，有緣千里來相會，無緣當面不相識，從此，你的面容便深藏在我的腦海，揮之不去。多少個夢裡，與你攜手並肩而坐，觀賞夕陽下的餘暉，聆聽駭浪拍打海岸的壯麗，漫步於馨香的花卉中，於花朵竊竊私語，觀蝶嬉鬧追逐的浪漫。
```
Output:
```
人生幾何，夕陽幾度
不經意間的一次擦肩而過
都會成為我們記憶中最靚麗的一道風景
有緣千里來相會，無緣當面不相識，從此
你的面容便深藏在我的腦海，揮之不去
多少個夢裡，與你攜手並肩而坐
觀賞夕陽下的餘暉
聆聽駭浪拍打海岸的壯麗
漫步於馨香的花卉中，於花朵竊竊私語
觀蝶嬉鬧追逐的浪漫
```

## Run
```bash
python main.py [input text file path] [output text file path]
```
