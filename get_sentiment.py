import argparse
import requests


def get_review(review_type):
    """Returns review of specified type."""
    reviews = {
        'positive': 'I loved the movie, I will most likely watch it again with great pleasure :) .',
        'negative': 'I was really bored, the acting was mediocre, almost fell asleep, unpleasant experience.'
    }

    if review_type in reviews.keys():
        return reviews[review_type]
    else:
        raise Exception('Wrong type: {}'.format(review_type))


def run_request(review, url):
    """Runs a request and prints results."""
    try:
        r = requests.post(url, json={'text': review}).json()
    except requests.exceptions.ConnectionError:
        print('Start the server first.')
        exit()

    if r['success']:
        print(r['predictions'])
    else:
        print('Request failed')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_inference_url", type=str, default='http://localhost:5000/predict',
                        help="Prediction URL")
    parser.add_argument("--review_type", type=str, required=True,
                        help="Type of review: positive, neutral, negative.")
    args = parser.parse_args()

    review = get_review(args.review_type)
    print('Review:\n', review)
    run_request(review, args.api_inference_url)
