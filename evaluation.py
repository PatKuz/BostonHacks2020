import sys, yaml
from google.cloud import automl

def get_prediction(file_path):
    prediction_client = automl.PredictionServiceClient()
    creds = yaml.safe_load(open("creds.yaml", "r"))
    project_id = creds['PROJ_ID']
    model_id = creds['MODEL_ID']

    with open(file_path, 'rb') as ff:
        content = ff.read()

    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content }}
    params = {"score_threshold": "0.501"}
    request = automl.PredictRequest(
        name=name,
        payload=payload,
        params=params
    )
    response = prediction_client.predict(request=request)
    coords = []
    pred = ''
    for item in response.payload:
        for vert in item.image_object_detection.bounding_box.normalized_vertices:
            coords.append(vert)
        pred = item.display_name
    if pred!='':
        return pred,coords[0].x,coords[0].y,coords[1].x,coords[1].y
    else:
        return None
