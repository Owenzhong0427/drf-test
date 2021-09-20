def root(request):
    if request.user.is_authenticated:
        return redirect('api-docs:docs-index')

    return JsonResponse({'name': 'Owen DRF API'})