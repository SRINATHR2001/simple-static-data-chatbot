import re
import long_responses as long

def message_probability(user_message, recognised_words, singleresponse=False, required_words=[] ):
    message_certainity =0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainity+=1
  
    percentage = float(message_certainity) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break
    
    if has_required_words or singleresponse:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list ={}

    def response(bot_response, list_of_words, singleresponse=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, singleresponse, required_words)

    #responses____________________________________________________________________________________
    response("hello!",['hi','hello','yo','whatsup'],singleresponse=True)
    response("i\'m doing fine!",['how','are','you','doing'],required_words=['how','you','doing'])
    response("me too ",['i','like','you'])
    response(long.b_eating,['what','are', 'you','eating'],required_words=['you','eating'])
     
    best_match = max(highest_prob_list,key=highest_prob_list.get)


    return long.unknown() if highest_prob_list[best_match] <1 else best_match
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?.-]\s*',user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    print('bot: '+get_response(input('you: ')))
