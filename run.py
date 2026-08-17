from app import create_app
import os
# from .app.provider.polza import PolzaProvider

# provider = PolzaProvider(
#     api_key=os.getenv('POLZA_API_KEY'),
#     base_url=os.getenv(''),
#     model=os.getenv('POLZA_MODEL'),
#     language=os.getenv(''),
#     timeout_seconds=os.getenv(''),
# )
app = create_app()

app.run()
