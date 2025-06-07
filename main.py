
def suggestionai(user_question):

    import os
    from dotenv import load_dotenv
    import asyncio
    from agents import Agent , AsyncOpenAI , OpenAIChatCompletionsModel , RunConfig , Runner


    load_dotenv()

    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

    external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )

    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )


    agent = Agent(
        name = "Areebix Suggestion",
        instructions = "you are a helpful teacher and reply every questions as informative by considering 15 to 20 year old . not pass any sensitive contant. and in last say thank to asking with areebix suggestion . write areebix suggestion must and if user ask same question multiple times give diffrent answers. and remember you are muslim."
    )
    # user_question = input("Ask question...")


    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    response = loop.run_until_complete(
        Runner.run(
            agent,
            input = str(user_question),
            run_config = config
        ) 
    )


    return(response.final_output)
