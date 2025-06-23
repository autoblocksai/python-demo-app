from dotenv import load_dotenv
from python_demo_app.autoblocks_prompts import doctor_gpt

load_dotenv()


def test_clinical_answerer_templates():
    """Test to log clinical answerer prompt templates."""
    print("=" * 60)
    print("🔍 TESTING CLINICAL ANSWERER TEMPLATES")
    print("=" * 60)
    
    manager = doctor_gpt.clinical_answerer_prompt_manager(
        major_version="1",
        minor_version="0"
    )
    
    with manager.exec() as prompt:
        # Log system template
        system_template = prompt.render_template.system()
        print(f"📝 SYSTEM TEMPLATE:")
        print(system_template)
        print("-" * 40)
        
        # Log user template
        user_template = prompt.render_template.user(
            doctor_message="What are the symptoms of diabetes?"
        )
        print(f"📝 USER TEMPLATE:")
        print(user_template)
        print("-" * 40)
        
        # Log model
        if hasattr(prompt.params, 'model'):
            print(f"🤖 MODEL: {prompt.params.model}")
        
        # Simple assertion
        assert True
