# Pixel Perfect Tree Job Application

## Model a Blog Application

Your task is to create class/classes in `Ruby` or `JavaScript` (or any language, really) to model a blog application.

- Create the needed class/classes to read the post.json file described below and create as many objects as you think you'll need from it to accomplish the following:

  * Find `Post` by ID
  * Find `Posts` by Author
  * Find `Posts` by Tag (Takes only 1 Tag and returns each post with the given Tag)
  * Find all `Tags` of Posts List along with the frequency
  * Display only the first 10 words from the description.

- Create a Web App (Rack/Sinatra/Flask) App that takes the posts.json file described below which contains multiple `Post` and serve posts through an end point on the application. Example: http://your.app/posts/1 and respond with an HTML displaying the attributes of the post with ID 1 of the JSON.

Bonus points for:

* **Testing your code.** 

* UI Details (Nothing fancy, just something that will let us know that you can work your way around HTML/CSS)

* Showing all posts of a tag and/or author on end point. EG: http://your.app/tags/cooking `||` http://your.app/tags/pixelator

* Showing your Git knowledge.
