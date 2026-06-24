"""
Minimal API entrypoint for Vercel.
The actual web tool is in index.html (static).
This file exists only to satisfy Vercel's Python detection.
"""

def handler(request):
    """Placeholder handler - not used since we're serving static HTML"""
    return {
        'statusCode': 404,
        'body': 'Use index.html instead',
        'headers': {'Content-Type': 'text/plain'}
    }
