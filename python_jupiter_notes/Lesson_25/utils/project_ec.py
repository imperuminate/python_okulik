# Project expected conditions

def text_is_not_empty_in_element(element): #Custom method fot WebDriverWait. Cool!!
    def _predicate(_):
        if len(element.text) > 0:
            return True
        else:
            return False
    return _predicate

