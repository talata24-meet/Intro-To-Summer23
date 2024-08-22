def create_youtube_video(title,desc):
	youtube_video = {"title":title, "description":desc, "likes":0, "dislikes":0, 
"comments":{}}
	return youtube_video

def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1
	return youtube_video

def dislikes(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]+=1

def add_comment(youtube_video,username,comment_text):
	if "comments" in youtube_video:
		youtube_video["comments"][username]= comment
	return video

myVideo=create_youtube_video("lol", "womp womp")
myVideo=like(myVideo)
myVideo=dislikes(myVideo)
myVideo=add_comment(myVideo)
print(myVideo)