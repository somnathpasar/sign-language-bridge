from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.sign_predictor import predict_sign
from app.services.tts_service import speak
from app.services.phrase_mapper import get_phrase


router = APIRouter()


@router.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    image = await file.read()


    sign = predict_sign(
        image
    )


    phrase = get_phrase(
        sign
    )


    if sign != "No hand detected":

        speak(
            phrase
        )


    return {

        "prediction": sign,

        "message": phrase
    }