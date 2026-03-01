def compute_priority(transformer_score, sender_score,
                     keyword_score, thread_score, calendar_score):

    importance = (
        0.35 * transformer_score +
        0.20 * sender_score +
        0.15 * keyword_score +
        0.15 * thread_score +
        0.10 * calendar_score
    )

    if importance > 0.8:
        return "Very Important"
    elif importance > 0.5:
        return "Medium Important"
    else:
        return "Not Important"
