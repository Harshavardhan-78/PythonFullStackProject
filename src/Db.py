from supabase import create_client
from src.Logic import get_settings

settings = get_settings()
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
