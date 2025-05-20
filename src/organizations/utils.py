from .models import Activity



def get_all_children(activity: Activity):
    ids = [activity.id]
    for child in activity.children:
        if child.children:
            ids.extend(get_all_children(child))
        ids.append(child.id)

    return ids
        
