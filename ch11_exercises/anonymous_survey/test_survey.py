from survey import AnonymousSurvey; import pytest

@pytest.fixture
def language_survey():
    """A survey available to all test functions"""
    question = "What language did you learn first to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test one response is stored properly"""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test three individual responses are stored properly"""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses