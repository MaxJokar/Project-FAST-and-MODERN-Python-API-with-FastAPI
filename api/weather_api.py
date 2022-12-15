import fastapi
from typing import Optional
from models.location import Location
from models.umbrella_status import UmbrellaStatus
import httpx

router = fastapi.APIRouter()


@router.get("/api/umbrella", response_model=UmbrellaStatus)
# def need_umbrella(city: str, country: str = "DE", state: Optional[str] = None):
async def do_i_need_umbrella(location: Location = fastapi.Depends()):
    url = f"https://weather.talkpython.fm/api/weather?city={location.city}\
    &country={location.country}& units=imperial"
    if location.state:
        url += f"&state={location.state}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()
        # get data
        print(resp.text)
    weather = data.get("weather", {})
    category = weather.get("category", "UNKNOWN")

    forecast = data.get("forecast", {})
    temp = forecast.get("temp", 0.0)

    bring = category.lower().strip() == "rain"
    umbrella = UmbrellaStatus(bring_umbrella=bring, temp=temp, weather=category)

    # print(resp.status_code)
    # print(resp.text)

    return umbrella
