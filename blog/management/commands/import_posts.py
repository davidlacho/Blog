import datetime
from django.core.management.base import BaseCommand
from blog.models import Author, Post


class Command(BaseCommand):
    help = "Imports posts from a predefined list"

    def handle(self, *args, **options):
        all_posts = [
            {
                "slug": "tech-trends-2024",
                "title": "Emerging Tech Trends in 2024",
                "image": "tech-trends.jpg",
                "excerpt": "Explore the cutting-edge technologies that are set to shape our future in 2024.",
                "content": """As technology continues to evolve at an unprecedented rate, keeping up with the latest trends is more important than ever. In 2024, several key technologies are set to make a significant impact across various industries.

Artificial intelligence (AI) continues to lead the way, with advancements in machine learning algorithms and AI-driven automation transforming how businesses operate. Blockchain technology is also gaining traction, offering more secure and decentralized solutions for transactions and data storage.

In the realm of consumer electronics, augmented reality (AR) and virtual reality (VR) are becoming increasingly mainstream, providing immersive experiences that were once the stuff of science fiction. Additionally, the Internet of Things (IoT) is expanding its reach, connecting more devices and enabling smarter homes and cities.

These technologies are not just changing the business landscape; they're also shaping the way we live, work, and interact with the world around us. As we look to the future, it's clear that embracing these trends will be crucial for staying ahead in an ever-evolving world.""",
                "author": "David",
                "date": datetime.date(2024, 5, 5),
            },
            {
                "slug": "home-gardening-101",
                "title": "Home Gardening for Beginners",
                "image": "gardening.jpg",
                "excerpt": "Discover the joys of gardening with our beginner's guide to creating your own green space.",
                "content": """Gardening is not only a relaxing hobby but also a way to enhance your environment and grow your own food. This guide will help beginners understand the basics of setting up a garden at home.

Starting with selecting the right location, to choosing plants suitable for your climate, and basic maintenance tips, we cover all you need to know to start your gardening journey. We also dive into the benefits of organic gardening, teaching you how to avoid chemicals in favor of natural solutions.

Whether you have a small balcony or a large backyard, this guide provides practical advice that will help you grow a thriving garden. Get ready to get your hands dirty and enjoy the fruits (and vegetables!) of your labor.""",
                "author": "David",
                "date": datetime.date(2024, 4, 20),
            },
            {
                "slug": "mindfulness-meditation",
                "title": "Mindfulness and Meditation",
                "image": "meditation.jpg",
                "excerpt": "Learn how mindfulness meditation can enhance your daily life and bring you peace.",
                "content": """Mindfulness meditation is a powerful practice that can help reduce stress, improve concentration, and promote a greater sense of well-being. In this article, we explore the basic techniques of mindfulness meditation and how you can incorporate them into your daily routine.

By focusing on your breath and observing your thoughts without judgment, mindfulness meditation encourages you to live in the present moment. This can lead to a reduction in anxiety and an overall enhancement in life satisfaction.

We'll provide tips on creating a conducive environment for meditation, establishing a routine, and overcoming common challenges that beginners face. Embrace the calm and clarity that mindfulness meditation offers and start seeing the positive changes in your life.""",
                "author": "David",
                "date": datetime.date(2024, 5, 1),
            },
            {
                "slug": "diy-home-decor",
                "title": "DIY Home Decor Ideas",
                "image": "home-decor.jpg",
                "excerpt": "Transform your space with these easy and affordable DIY home decor ideas.",
                "content": """Looking to spruce up your home without breaking the bank? Our DIY home decor ideas are not only cost-effective but also add a personal touch to your living space.

From repurposing old furniture to creating beautiful wall art, we provide step-by-step guides that make it easy for anyone to get involved in home decoration. Learn how to use colors, textures, and patterns to enhance the aesthetics of your rooms.

This article is perfect for those who love crafting and are eager to personalize their home. Get inspired by our creative ideas and start transforming your space today!""",
                "author": "David",
                "date": datetime.date(2024, 5, 3),
            },
            {
                "slug": "healthy-eating-habits",
                "title": "Building Healthy Eating Habits",
                "image": "healthy-eating.jpg",
                "excerpt": "Learn how to develop healthy eating habits that will last a lifetime.",
                "content": """Eating healthy isn't just a diet; it's a lifestyle. In this article, we explore practical tips for building healthy eating habits that you can maintain over the long term.

We discuss the importance of balancing macronutrients, choosing whole foods over processed options, and the benefits of mindful eating. Additionally, we provide advice on planning meals and making smart food choices while dining out.

By making informed decisions about your diet, you can improve your health, boost your energy levels, and even manage your weight. Start your journey towards a healthier life today by adopting these simple yet effective eating habits.""",
                "author": "David",
                "date": datetime.date(2024, 4, 25),
            },
        ]

        for entry in all_posts:
            author_name = entry["author"].split()
            author, created = Author.objects.get_or_create(
                first_name=author_name[0],
                last_name=author_name[1] if len(author_name) > 1 else "",
                defaults={"email_address": f"{author_name[0].lower()}@example.com"},
            )

            post, created = Post.objects.update_or_create(
                slug=entry["slug"],
                defaults={
                    "title": entry["title"],
                    "excerpt": entry["excerpt"],
                    "image_name": entry["image"],
                    "content": entry["content"],
                    "date": entry["date"],
                    "author": author,
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created post: {post.title}")
                )
            else:
                self.stdout.write(f"Updated post: {post.title}")
