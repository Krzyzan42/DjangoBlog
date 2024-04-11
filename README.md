# Introduction
This is a blog website written using Django, it's based on an <a href="https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p">online tutorial</a> . Link to the website: http://www.blog.krzyzan.xyz, be sure to connect using http, some browsers like to force https. The server is running on Apache on a virtual linux server, and it was configured entirerly throught a SSH connection. And don't worry, on the real server settings have been changed to be secure.
![image](https://github.com/Krzyzan42/blog_tutorial/assets/100627976/87b90417-0f35-44eb-857c-5946f05ea377)

# Why it looks so bad
This project is kinda old and relies heavily on bootstrap to style elements. At some point either boostrap got updated or I changed its version, and now some of the style rules got lost. I don't want to update it though, I have more important things to do atm.

# Features
### Users
Users can register, log in, edit their information and profile picture. They can also create posts. On the debug version, there's an option to reset your password from the link sent to your email, but I disabled it on the actual website.

### Posts
Posts can be created, updated and deleted by users who made them. If you click on a user profile on a post, you filter the posts by selected users. If there are too many posts, they get paginated.
