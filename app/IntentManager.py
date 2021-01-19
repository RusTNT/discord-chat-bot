import dialogflow_v2 as dialogflow


class IntentManager:
    def __init__(self, project_id):
        self.project_id = project_id

    def detect_texts(self, texts, session_id, lang):
        self.texts = texts
        self.session_id = session_id
        self.lang = lang

        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(self.project_id, self.session_id)

        for text in self.texts:
            text_input = dialogflow.types.TextInput(text=text, language_code=self.lang)
            query_input = dialogflow.types.QueryInput(text=text_input)
            response = session_client.detect_intent(session=session, query_input=query_input)

            return [response.query_result.query_text,
                    response.query_result.intent.display_name,
                    response.query_result.intent_detection_confidence,
                    response.query_result.fulfillment_text]
