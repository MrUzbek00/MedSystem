def extradata(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'doctor':
            return {
                'head':request.user.department.all().exists()
            }
    return{}
