from .models import Post, PostAnalysis
from .exceptions import InvalidAnalysisTask


def create_analysis(post_id):
        post = Post.objects.get(id=post_id)
        words = post.content.split(' ')
        word_count = len(words)
        word_sizes = [len(w) for w in words]
        average_word_size = sum(word_sizes) / word_count

        post_analysis = PostAnalysis.objects.create(
            post_id=post,
            word_count=word_count,
            average_word_size=average_word_size)

        return post_analysis
