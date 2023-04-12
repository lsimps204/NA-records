def map_json_data_to_modelfields(record_data) -> dict:
    """ Takes the JSON data from NA API, and maps the structure to a flat format suitable
        for passing directly to the Django Record model.
    """
    return {
        "id": record_data.get("id"),
        "title": record_data.get("title"),
        "citable_reference": record_data.get("citableReference"),
        "description": record_data.get("scopeContent", {}).get("description"),
    }