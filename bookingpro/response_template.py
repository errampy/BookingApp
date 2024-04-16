def response_template(status, message=None):
    '''
    desc : This function is responsible to return the response message, 

    Args:
    status : this parameter must be boolean like True or False
    message : This should be string or any message
    '''
    response = {
        'status' : status,
        'message' : message,
    }
    return response