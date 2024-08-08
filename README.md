### WORK IN PROGRESS ###

ShadCn components rewritten using Python, htmx, tailwindcss and javascript to be a fully-functioning drop-in plugin for fastHTML. With minor tinkers to your python files (mainly js and htmx), you can have access to a range of functionality that resembles Shadcn's ui components, However with a single header function and import statement, you have access to the entire styled library off the bat! Minor tweaks to htmx and some js scripts can augment your components to new levels, its entirely up to you. Due to the open-source nature of Shadcn's ui library, this library will also be completely open source and the code is yours to copy/ modify/ change as you like.

Tailwind-merge has not been added as of yet, so if you find your custom tailwind classes for the components not altering their style, add an '!' before the classname, i.e "class=!w-full". This tells tailwind that this class is important, and to override the underlying width setting properties. It is not a perfect fix, but will help you with your styling flow until I have added it.

To get started, copy the shadcn.py file into your repository, add "from shadcn import *" to the top of the file you wish to use it in, and add "ShadHead()" into your hdrs variable within either FastHTML() or the fast_app() functions. Imports are automatically written over from the fasthtml.common package, meaning you can start straight away by writing your ft components!

Syntax is very straight forward, let's take the card component for example. 
You can render it using the familiar fasthtml format: 

`return Card("Content goes here", header="Header title", description="Card description", footer="Footer here")`

Alternatively, if you're more comfortable following the original shadcn component syntax, then you can do that too:

`return Card(CardHeader(CardTitle("Title Here"), CardDescription("Description Here")), CardContent("Content Here"), CardFooter("Footer Here"))`

Whichever option you prefer is available, so its your choice as to which you prefer. I am currently working on porting the entire components library over, along with hopefully some extra components and functionality that will prove useful in full scale UI boilerplating and enhancement, out of the box.

Any recommendations, tweaks or feedback, please do create a pull request or simply send me a message. Although I have decent experience in web development, I'm still learning python as I go so any help would be greatly appreciated - cheers

All credits go to @Shadcn for his incredible component library, tailwindcss for making styling so much easier, and of course @JeremyPHoward for his insane work making the fasthtml framework.