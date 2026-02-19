def get_response(score: int, hints_used: int) -> dict:
    return {
        'message': f'Your score is {score}. You have used {hints_used} hints.',
        'hints_remaining': max(0, 3 - hints_used)
    }
