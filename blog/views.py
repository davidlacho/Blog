from datetime import date
from django.http import Http404
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "title": "Mountain Hiking",
        "image": "mountains.jpg",
        "excerpt": "There's nothing like the views you get like when you're hiking in the mountains and I wasn't prepared for what happened while I was enjoying the view",
        "content": """Embarking on a mountain hike is embarking on a journey into the heart of nature's grandeur. With every step, the landscape unfolds before you like a magnificent painting, each peak and valley a testament to the Earth's enduring beauty. The air is crisp, carrying the scent of pine and adventure, while the trail winds its way through rugged terrain and lush forests.

It was on one such hike that I found myself utterly captivated by the sheer majesty of the mountains. As I ascended higher and higher, the world below seemed to shrink, replaced by an endless expanse of sky and rock. With each passing moment, I felt more alive, more connected to the earth and to myself.

But it wasn't just the scenery that left me breathless—it was what happened next. As I reached the summit and gazed out at the breathtaking vista before me, a sense of profound gratitude washed over me. In that moment, I realized just how small we are in the grand scheme of things, and yet how infinitely blessed we are to be a part of it all.

So, if you ever find yourself in need of a reminder of life's beauty and wonder, I highly recommend heading for the hills. There's nothing quite like the views you get when you're hiking in the mountains, and I, for one, am forever grateful for the experience.
""",
        "author": "David",
        "date": date(2021, 7, 21),
    },
    {
        "slug": "programming-is-fun",
        "title": "Programming is Great",
        "image": "coding.jpg",
        "excerpt": "Some people think that programming is hard and boring but I think it's fun and I want to tell you why",
        "content": """Programming isn't just about writing lines of code—it's about crafting solutions to complex problems, building digital worlds from scratch, and unleashing your creativity in ways you never thought possible. While some may see it as daunting or tedious, I find programming to be an endlessly fascinating pursuit, filled with excitement and discovery at every turn.

For me, the joy of programming lies in the thrill of bringing ideas to life, of seeing lines of code transform into functional, interactive software. Whether it's designing a sleek user interface, optimizing algorithms for maximum efficiency, or debugging that pesky piece of code that just won't work, there's always something new to learn and explore.

But perhaps the greatest reward of programming is the sense of empowerment it brings. In a world increasingly driven by technology, the ability to code opens doors to endless possibilities, from creating your own apps and games to solving real-world problems and making a positive impact on the world around you.

So, if you've ever been curious about programming but hesitated to give it a try, I encourage you to take the plunge. You might just discover that what some see as hard and boring is, in fact, one of the most fun and rewarding pursuits out there.
""",
        "author": "David",
        "date": date(2021, 9, 15),
    },
    {
        "slug": "into-the-woods",
        "title": "Nature Walks",
        "image": "woods.jpg",
        "excerpt": "Nature walks help me de-stress after a long week of work. I always return home feeling fresh and with a new persective on things",
        "content": """In the heart of the woods, amidst towering trees and the symphony of birdsong, lies a sanctuary of tranquility waiting to be discovered. Nature walks, with their gentle pace and breathtaking scenery, offer a much-needed respite from the hustle and bustle of daily life. With each step, the stresses of the week melt away, replaced by a profound sense of peace and connection to the natural world.

For me, a nature walk is more than just a leisurely stroll—it's a form of therapy, a chance to recharge and reset amidst the beauty of the great outdoors. Surrounded by the sights and sounds of the forest, I find myself breathing more deeply, moving more slowly, and simply being present in the moment.

And it's not just my mood that benefits from these excursions into nature. Studies have shown that spending time outdoors can have a positive impact on both physical and mental well-being, from reducing stress and anxiety to boosting mood and creativity.

So, the next time you find yourself feeling overwhelmed or burnt out, why not lace up your hiking boots and head for the nearest trail? You may be surprised at the transformative power of a simple walk in the woods.
""",
        "author": "David",
        "date": date(2021, 10, 22),
    },
    {
        "slug": "rafting-in-the-rapids",
        "title": "Rafting Adventures",
        "image": "rafting.jpg",
        "excerpt": "Rafting is one of my favorite activities because it's fun and it gets your adrenaline pumping. It's an experience like no other",
        "content": """Feel the rush of adrenaline as you navigate roaring rapids, the thrill of conquering the untamed power of nature, the camaraderie of fellow adventurers by your side—rafting is not just an activity, it's an adventure like no other. From the moment you push off from the shore to the final exhilarating splash, every moment on the water is filled with excitement and possibility.

For me, rafting is more than just a hobby—it's a way of life, a source of endless joy and inspiration. Whether I'm paddling through swirling whitewater or drifting lazily downstream, there's a sense of freedom and exhilaration that can't be matched by any other experience.

But perhaps the greatest reward of rafting is the connection it fosters with the natural world. In a society increasingly detached from the rhythms of nature, rafting offers a rare opportunity to immerse oneself fully in the beauty and power of the great outdoors, to feel the pulse of the river beneath you and the sun on your face.

So, if you're looking for a truly unforgettable adventure, why not grab a paddle and join me on the river? You never know what wonders await just around the bend.
""",
        "author": "David",
        "date": date(2021, 11, 2),
    },
    {
        "slug": "peaceful-meditation",
        "title": "The Peace of Meditation",
        "image": "meditation.jpg",
        "excerpt": "Discover the profound calm and clarity that comes from meditation. I wasn't prepared for the transformative effect it had on me during a serene beach session.",
        "content": """In a world filled with noise and distraction, meditation offers a sanctuary of stillness—a chance to quiet the mind, calm the body, and connect with the present moment in all its richness and complexity. Whether you're sitting cross-legged on a cushion, walking mindfully along a beach, or simply taking a few deep breaths at your desk, the practice of meditation has the power to transform your life in ways you never thought possible.

For me, meditation is not just a technique—it's a way of being, a path to inner peace and self-discovery that unfolds with each breath. During a recent meditation session on a serene beach, I experienced a profound sense of clarity and connection that stayed with me long after the session ended. As the waves gently lapped at the shore and the sun dipped below the horizon, I felt a deep sense of gratitude for the beauty of the world and the gift of being alive.

But perhaps the most remarkable thing about meditation is its accessibility. You don't need fancy equipment or years of training to experience its benefits—all you need is a willingness to sit quietly and pay attention to the present moment. So why not give it a try? You may be surprised at the peace and clarity that await you, just beneath the surface of your busy mind.
""",
        "author": "David",
        "date": date(2020, 11, 2),
    },
]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=lambda post: post["date"], reverse=True)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    try:
        post = next(post for post in all_posts if post["slug"] == slug)
        return render(request, "blog/post-detail.html", {"post": post})
    except StopIteration:
        raise Http404("Post Not Found")
