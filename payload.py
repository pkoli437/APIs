{
    "created_by": "admin_user",
    "user_id": "u123",
    "dialer": "voice_dialer_v1",
    "flow_type": "support_flow",
    "agent_name": "HelpDeskAgent",
    "agent_type": "AI",
    "sts_model_id": "sts-2024",
    "sts_model_perms": {
        "read": true,
        "write": false,
        "execute": false
    },
    "llm_model_id": "gpt-4.0",
    "llm_model_param": {
        "temperature": 0.8,
        "max_tokens": 1000
    },
    "llm_model_document": "doc-456",
    "tts_model_id": "tts-en-01",
    "tts_model_perm": {
        "speak": true,
        "translate": false
    },
    "nodes": {
        "start": {
            "id": 1,
            "type": "start",
            "description": "Beginning of the flow"
        },
        "ask_name": {
            "id": 2,
            "type": "input",
            "prompt": "What is your name?"
        },
        "end": {
            "id": 3,
            "type": "end",
            "description": "Conversation complete"
        }
    }
}
