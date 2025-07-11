#Write a program to find out whether a given post is talking about "Kanishk" or not

post = input("Enter the post: ")

if("Kanishk".lower() in post.lower()):
    print("This post is talking about Kanishk")
else:
    print("This post is not talking about Kanishk")