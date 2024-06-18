from math import *
import time
from typing import Any,List,Literal,Iterable
def is_prime(number:int) -> bool:
    if number == 1:
        return False
    for i in range(2,int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True
def is_odd(number:int) -> bool:
    if number%2==1:
        return True
    return False
def is_even(number:int) -> bool:
    if number%2==0:
        return True
    return False
def find_factor(number:int) ->list:
    back_lst=[]
    if type(number)!=int:
        raise TypeError("function 'find_factor' only can find factors of type 'int'")
    if number<1:
        raise ValueError("function 'find_factor' can't find its factor")
    if is_prime(number):
        return [1,number]
    for i in range(1,number+1):
        if number % i == 0:
            back_lst.append(i)
    
    return back_lst
def find_prime_factor(number:int,do_return_tuples:bool=False) -> (list[tuple[int,int]] | list):
    back_lst=[]
    another_lst=[]
    if type(number)!=int:
        raise TypeError("function 'find_factor' only can find factors of type 'int'")
    if number<2:
        raise ValueError("function 'find_factor' can't find its factor")
    num=number+1-1
    if is_prime(number):
        if do_return_tuples:
            return [(number,1)]
        else:
            return[number]
    while num!=1:
        for i in range(2,num):
            if num % i == 0 and is_prime(i):
                another_lst.append(i)
                num//=i
                if is_prime(num):
                    another_lst.append(num)
                    break
        if is_prime(num):
            break
    if not do_return_tuples:
        return another_lst
    for i in another_lst:
    
        c=another_lst.count(i)
        back_lst.append((i,c))
        for _ in range(c):
            another_lst.remove(i)
    

    return back_lst
def co_prime(a:int,b:int) -> bool:
    if set(find_factor(a))&set(find_factor(b))=={1}:
        return True
    return False
def generate_prime_list(start:int,end:int,IncludeStop:bool=True) -> list:
    if IncludeStop:
        my_range=range(start,end+1)
    else:
        my_range=range(start,end)
    back_list=[]
    for i in my_range:
        if is_prime(i):
            back_list.append(i)
    return back_list
def cut_float(a_float:float) -> int:
    return int(str(a_float).split('.')[0])
def get_minus(a_list:list) -> list[int]:
        return [b-s for s,b in zip(a_list[:-1:],a_list[1::])]
def sum_multiply(thing:Iterable[int]) -> int:
    a=1
    for i in thing:a*=i
    return a
def lowest_common_multiple(*numbers:int) -> int:
    numbers=list(numbers)
    if len(numbers)==2:
        if co_prime(numbers[0],numbers[1]):
            return sum_multiply(numbers)
        my_lst1=[i for i in find_prime_factor(numbers[0])]
        my_lst2=[i for i in find_prime_factor(numbers[1])]
        bind_list=[]
        # for i in find_prime_factor(numbers[0]):
        #     my_lst1.append(i)
        # for i in find_prime_factor(numbers[1]):
        #     my_lst2.append(i)
        my_lst1_a=my_lst1.copy();my_lst2_a=my_lst2.copy()
        for i in my_lst1_a:
            if (i in my_lst1) and (i in my_lst2):
                my_lst1.remove(i);my_lst2.remove(i);bind_list.append(i)
        for i in bind_list:
            my_lst1_a.remove(i)
        return sum_multiply(my_lst2_a+my_lst1_a)
    else:
        a=lowest_common_multiple(*(numbers[1::]))
        return lowest_common_multiple(numbers[0],a)
def greatest_common_divisor(*numbers : int) -> int:
    numbers=list(numbers)
    
    if len(numbers)==2:
        if co_prime(numbers[0],numbers[1]):
            return 1
        my_lst1=[i for i in find_prime_factor(numbers[0])]
        my_lst2=[i for i in find_prime_factor(numbers[1])]
        bind_list=[]
        # for i in find_prime_factor(numbers[0]):
        #     my_lst1.append(i)
        # for i in find_prime_factor(numbers[1]):
        #     my_lst2.append(i)
        my_lst1_a=my_lst1.copy();my_lst2_a=my_lst2.copy()
        for i in my_lst1_a:
            if (i in my_lst1) and (i in my_lst2):
                my_lst1.remove(i);my_lst2.remove(i);bind_list.append(i)
        return sum_multiply(bind_list)
    else:
        a=greatest_common_divisor(*(numbers[1::]))
        return greatest_common_divisor(numbers[0],a)
def get_multiple(a_list:list) -> list:

    return [b/s for s,b in zip(a_list[:-1:],a_list[1::])]
def find_perfect_number(number_to = 6) -> list[int]: # include number_to
    '''
    include number_to
    '''
    back_list=[]
    if number_to>=6:
        try_number=1
        while (2**try_number-1)*(2**(try_number-1))<=number_to:
            if is_prime(2**try_number-1):
                back_list.append((2**try_number-1)*(2**(try_number-1)))
            try_number+=1
        return back_list

    else:
        return []
def is_perfect_number(number:int=None) -> bool:
    sums=0
    for ij in find_factor(number):
        if ij!=number:
            sums+=ij
    if sums==number:
        return True
    return False
def is_iterable(thing:Any) -> bool:
    try:
        thing.__iter__()
        return True
    except:
        return False
def turn_float_into_int(iterable:Iterable[float]) -> Iterable[int|float]:
    for num,i in enumerate(iterable):
        if int(i)==i:
            iterable[num]=int(i)
    return iterable
class CantFindPatternError(BaseException):
    ...
def find_pattern(lst:list,continue_steps:int=1):
    if len(lst)<=3:
        raise CantFindPatternError("can't find pattern with list which its length is smaller than 4")
    def fun1():
        counter=0
        for s,b in zip(lst[:-1:],lst[1::]):
            if s == lst[0]:
                p=b-s;counter+=1
            else:
                if b-s==p:
                    counter+=1
        if counter==len(lst)-1:
            raise Exception([1 , p , lst[-1]])
        '''------等差数列------'''
    def fun2():
        counter=0
        for s,b in zip(lst[:-1:],lst[1::]):
            if s == lst[0]:
                p=b/s;counter+=1
            else:
                if b/s==p:
                    counter+=1
        if counter==len(lst)-1:
            raise Exception([2 , p , lst[-1]])
        '''------等比数列------'''
    def fun3():
        minus_list=get_minus(lst)
        counter=0
        for s,b in zip(minus_list[:-1:],minus_list[1::]):
            if s == minus_list[0]:
                p=b-s;counter+=1
            else:
                if b-s==p:
                    counter+=1
        if counter==len(minus_list)-1:
            raise Exception([3 , p , lst[-1] , minus_list[-1]])
        '''------差中等差------'''
    def fun4():
        minus_list=get_minus(lst)
        counter=0
        for s,b in zip(minus_list[:-1:],minus_list[1::]):
            if s == minus_list[0]:
                p=b/s;counter+=1
            else:
                if b/s==p:
                    counter+=1
        if counter==len(minus_list)-1:
            raise Exception([4 , p , lst[-1] , minus_list[-1]])
        '''------差中等比------'''
    def fun5():
        multiple_list=get_multiple(lst)
        counter=0
        for s,b in zip(multiple_list[:-1:],multiple_list[1::]):
            if s == multiple_list[0]:
                p=b-s;counter+=1
            else:
                if b-s==p:
                    counter+=1
        if counter==len(multiple_list)-1:
            raise Exception([5 , p , lst[-1] , multiple_list[-1]])
        '''------比中等差------'''
    def fun6():
        multiple_list=get_multiple(lst)
        counter=0
        for s,b in zip(multiple_list[:-1:],multiple_list[1::]):
            if s == multiple_list[0]:
                p=b/s;counter+=1
            else:
                if b/s==p:
                    counter+=1
        if counter==len(multiple_list)-1:
            raise Exception([6 , p , lst[-1] , multiple_list[-1]])
        '''------比中等比------'''
    def fun7():
        if lst==generate_prime_list(lst[0],lst[-1]):
            raise Exception([7 , lst[-1]])
    def main():
        fun1()
        fun2()
        fun3()
        fun4()
        fun5()
        fun6()
        fun7()
        raise Exception([None])
    try:
        main()
    except Exception as stuff:
        stuff=str(stuff)
        back_lst=[]
        stuff=eval(stuff)
        match stuff[0]:
            case 1:
                for _ in range(continue_steps):
                    stuff[2]+=stuff[1]
                    back_lst.append(stuff[2])
            case 2:
                for _ in range(continue_steps):
                    stuff[2]*=stuff[1]
                    back_lst.append(stuff[2])
                back_lst=turn_float_into_int(back_lst)
            case 3:
                for _ in range(continue_steps):
                    stuff[3]+=stuff[1]
                    stuff[2]+=stuff[3]
                    back_lst.append(stuff[2])
            case 4:
                for _ in range(continue_steps):
                    stuff[3]*=stuff[1]
                    stuff[2]+=stuff[3]
                    back_lst.append(stuff[2])
            case 5:
                for _ in range(continue_steps):
                    stuff[3]+=stuff[1]
                    stuff[2]*=stuff[3]
                    back_lst.append(stuff[2])
            case 6:
                for _ in range(continue_steps):
                    stuff[3]*=stuff[1]
                    stuff[2]*=stuff[3]
                    back_lst.append(stuff[2])
            case 7:
                while len(back_lst)<continue_steps:
                    stuff[1]+=1
                    if is_prime(stuff[1]):
                        back_lst.append(stuff[1])
            case None:
                
                raise CantFindPatternError(f"can't find pattern of list -> {lst}")
        back_lst=turn_float_into_int(back_lst)
        return back_lst
words=['would', 'yes', 'garment', 'could', 'university', 'Mrs', 'Ms', 'Mr', 'alone', 'worse', 'full-time', 'worst', 'other', 'own', 'ripe', 'historical', 'short', 'outgoing', 'officious', 'silent', 'quiet', 'safe', 'secure', 'punctual', 'messy', 'Olympic', 'clerical', 'thin', 'valuable', 'protective', 'hopeful', 'violent', 'tragic', 'sad', 'northern', 'Arctic', 'shady', 'illogical', 'native', 'stupid', 'clumsty', 'comparative', 'relative', 'essential', 'compulsory', 'requisite', 'necessary', 'convenient', 'portage', 'cheap', 'user-friendly', 'superficial', 'outward', 'affectionate', 'sympathetic', 'freeze', 'uncommon', 'improbable', 'constant', 'unfair', 'unsmiling', 'illegal', 'unfit', 'rickety', 'casual', 'inevitable', 'tasteless', 'impossible', 'unhappy', 'unshakable', 'unacceptable', 'incredible', 'unrealistic', 'unwilling', 'doubtful', 'uncomfortable', 'diverse', 'different', 'watertight', 'secretive', 'careless', 'stale', 'unfortunate', 'stainless', 'weird', 'subtle', 'disused', 'abnormal', 'anonymous', 'scanty', 'dusty', 'part-time', 'financial', 'cruel', 'harsh', 'long', 'common', 'super', 'damp', 'wet', 'noisy', 'thorough', 'sunken', 'successful', 'mature', 'honest', 'urban', 'unrelenting', 'perpetual', 'dynamic', 'energetic', 'vigorous', 'pneumatic', 'noble', 'abstract', 'ugly', 'elementary', 'traditional', 'conventional', 'creative', 'vertical', 'pure', 'secondary', 'clever', 'intelligent', 'aerial', 'rude', 'coarse', 'crude', 'fragile', 'mistaken', 'false', 'wrong', 'bold', 'large', 'great', 'big', 'fussy', 'abundant', 'substantial', 'monotonous', 'separate', 'single', 'local', 'current', 'moral', 'low', 'hostile', 'resistant', 'junior', 'underground', 'Mediterranean', 'classic', 'typical', 'electrical', 'electronic', 'missing', 'eastern', 'steep', 'amused', 'independent', 'jealous', 'blunt', 'variable', 'multimedia', 'mountainous', 'cloudy', 'additional', 'extra', 'hungry', 'worried', 'mad', 'legal', 'properous', 'criminal', 'relaxed', 'earnest', 'remarkable', 'mobile', 'Afican', 'fertile', 'stout', 'crazy', 'sharp', 'sarcastic', 'auxiliary', 'rotten', 'nearby', 'complex', 'complicated', 'rich', 'wealthy', 'embarrassed', 'guilty', 'grateful', 'thankful', 'dry', 'clean', 'high', 'tall', 'delighted', 'glad', 'happy', 'merry', 'pleased', 'individual', 'personal', 'various', 'assorted', 'fundamental', 'inveterate', 'better', 'superior', 'public', 'official', 'lonely', 'ancient', 'classical', 'outlandish', 'eccentric', 'antique', 'solid', 'stubborn', 'deliberately', 'advisory', 'eerie', 'peculior', 'closed', 'bureaucratic', 'smooth', 'glorious', 'extensive', 'regular', 'expensive', 'international', 'national', 'civil', 'domestic', 'overzealous', 'excessive', 'allergic', 'past', 'overheated', 'naval', 'overseas', 'monstrous', 'outrageous', 'afraid', 'alcoholic', 'salty', 'rare', 'good', 'aggressive', 'hospitable', 'curious', 'amusing', 'intoxicated', 'logical', 'reasonable', 'fair', 'rational', 'appropriate', 'suitable', 'kind', 'peace', 'idyllic', 'dark', 'fine', 'yummy', 'frightened', 'overland', 'latter', 'thick', 'comic', 'humorous', 'chemcial', 'skeptial', 'pregnant', 'bad', 'desolate', 'absurd', 'ridiculous', 'royal', 'pale', 'dim', 'living', 'alive', 'mechanical', 'confidential', 'resourceful', 'active', 'positive', 'basic', 'breathtaking', 'senior', 'infinite', 'marvellous', 'fantastic', 'splendid', 'horrible', 'superb', 'tiny', 'disgusting', 'medical', 'collective', 'memorial', 'technical', 'skilful', 'insistent', 'determined', 'adamant', 'hard', 'indirect', 'tough', 'ardous', 'simple', 'straightforward', 'brief', 'architectural', 'healthy', 'forgetful', 'athletic', 'educational', 'inferior', 'minor', 'far', 'thrifty', 'following', 'shining', 'distinguished', 'golden', 'blonde', 'mere', 'urgent', 'relevant', 'tight', 'nervous', 'prudent', 'offshore', 'recent', 'approximate', 'progressive', 'economic', 'surprised', 'wonderful', 'lively', 'shrewd', 'spiritual', 'mental', 'competitive', 'motionless', 'upset', 'massive', 'enormous', 'huge', 'immense', 'tremendous', 'colossal', 'profound', 'qualified', 'concrete', 'specific', 'absolute', 'desperate', 'military', 'enlightened', 'invisible', 'visible', 'generous', 'considerate', 'roast', 'scientific', 'experimental', 'lovely', 'cute', 'lovable', 'accessile', 'alternative', 'feasible', 'cursed', 'available', 'honourable', 'wretched', 'possible', 'likely', 'forbidding', 'admirable', 'funny', 'reliable', 'optional', 'dubious', 'suspicious', 'objective', 'definite', 'blank', 'empty', 'spare', 'fanciful', 'vacant', 'thirsty', 'oral', 'spoken', 'dull', 'cheerful', 'gay', 'spacious', 'merciful', 'broad', 'wide', 'fanatical', 'ashamed', 'sleepy', 'difficult', 'lazy', 'romantic', 'old', 'optimistic', 'tired', 'cold', 'forbidding', 'theoretical', 'cubic', 'immediate', 'instant', 'prompt', 'successive', 'federal', 'joint', 'cool', 'vast', 'flexible', 'unpleasant', 'distasteful', 'awkward', 'amazing', 'awesome', 'staggering', 'troublesome', 'painful', 'repulsive', 'enjoyable', 'nice', 'impressive', 'pop', 'fluent', 'deaf', 'untidy', 'bare', 'naked', 'numb', 'full', 'contented', 'satisfied', 'slow', 'busy', 'feline', 'offensive', 'commercial', 'boring', 'unaware', 'worthless', 'impatient', 'annual', 'daily', 'everyday', 'weekly', 'beautiful', 'luscious', 'delicious', 'tasty', 'stuffy', 'lost', 'secret', 'intensice', 'dense', 'exempt', 'reluctant', 'facial', 'slim', 'slim', 'democratic', 'sensitive', 'bright', 'obvious', 'advisable', 'wise', 'sensible', 'vague', 'ambiguous', 'alien', 'indifferent', 'wooden', 'pastoral', 'durable', 'male', 'southern', 'abstruse', 'unbearable', 'inaccesible', 'inconceivable', 'untold', 'unbelievable', 'internal', 'inner', 'inward', 'able', 'muddy', 'elder', 'young', 'sticky', 'agricultural', 'female', 'European', 'fat', 'furnished', 'critical', 'remote', 'prety', 'poor', 'frequent', 'ordinary', 'parallel', 'average', 'battered', 'dilapidated', 'shabby', 'broken', 'widespread', 'universal', 'general', 'odd', 'strange', 'exotic', 'original', 'breathless', 'modest', 'humble', 'insidious', 'potential', 'shallow', 'greyish', 'embedded', 'mighty', 'strong', 'brilliant', 'dear', 'intimate', 'industrious', 'conscientious', 'slight', 'credulous', 'clear', 'distinct', 'explicit', 'emotional', 'sunny', 'comprehensive', 'entire', 'nationwide', 'overall', 'global', 'absent', 'lame', 'certain', 'true', 'awful', 'tropical', 'hot', 'eager', 'keen', 'enthusiastic', 'artificial', 'overpopulated', 'accepbtable', 'arbitrary', 'tolerant', 'easy', 'tedious', 'soft', 'sunburned', 'observant', 'upper', 'choice', 'elderly', 'addicted', 'extravagant', 'social', 'centigrade', 'physical', 'well', 'deep', 'tense', 'mysterious', 'holy', 'sacred', 'sick', 'ill', 'raw', 'vivid', 'vital', 'angry', 'rusty', 'blind', 'disappointed', 'intense', 'acute', 'severe', 'viritable', 'fashionable', 'practical', 'effect', 'prehistoric', 'annoying', 'agonizing', 'excitng', 'visual', 'moderate', 'applicable', 'chief', 'central', 'premier', 'popular', 'frightened', 'comfortable', 'familiar', 'multiple', 'digital', 'horizontal', 'underwater', 'asleep', 'submissive', 'private', 'rigid', 'dead', 'sensational', 'sour', 'acid', 'random', 'indiscriminate', 'overweight', 'Pacific', 'solar', 'greedy', 'greedily', 'corrupt', 'frank', 'escapist', 'tiresome', 'unusual', 'immaculate', 'special', 'particular', 'sore', 'inforative', 'manual', 'respectable', 'astronomical', 'challenging', 'usual', 'contemporary', 'miserable', 'transparent', 'abrupt', 'sudden', 'vain', 'oval', 'outer', 'foreign', 'external', 'bent', 'perfect', 'ideal', 'sheer', 'radical', 'utter', 'complete', 'identical', 'whole', 'late', 'insignificant', 'faint', 'microscopic', 'unique', 'only', 'loose', 'unable', 'unhurt', 'unforeseen', 'bitter', 'mild', 'warm', 'cosy', 'gentle', 'literary', 'steady', 'stable', 'uncertain', 'unimaginative', 'cordless', 'insoluble', 'insurmountable', 'innocent', 'rude', 'obscure', 'incompetent', 'endless', 'unconditional', 'unsympathetic', 'hopeless', 'useless', 'naïve', 'ignorant', 'unconscious', 'western', 'accustomed', 'fond', 'dramatic', 'systematic', 'narrow', 'cramped', 'downward', 'snowy', 'next', 'advanced', 'prior', 'previous', 'evident', 'apparent', 'noticeable', 'modern', 'ralistic', 'envious', 'dedicated', 'rural', 'considerable', 'equal', 'equivalent', 'contrary', 'related', 'contradictory', 'same', 'alike', 'similar', 'fragrant', 'elaborate', 'legendary', 'loud', 'like-minded', 'backward', 'rambling', 'desirable', 'decent', 'passive', 'negative', 'small', 'little', 'careful', 'cautious', 'miniature', 'efficient', 'evil', 'wicked', 'psychological', 'hard-working', 'new', 'fresh', 'excited', 'awake', 'fortunate', 'lucky', 'fierce', 'shy', 'weak', 'inflatable', 'pretentious', 'dizzy', 'academic', 'tame', 'rapid', 'quick', 'swift', 'Asia', 'strict', 'bored', 'woollen', 'distant', 'wild', 'amateur', 'sure', 'bound', 'agreement', 'consistent', 'smart', 'dependent', 'marriage', 'retired', 'former', 'prliamentary', 'uncanny', 'changeable', 'handy', 'delicate', 'aware', 'conscious', 'accidental', 'extraordinary', 'rainy', 'musical', 'disturbing', 'controversial', 'handsome', 'valiant', 'sweeping', 'worldwide', 'crowded', 'permanent', 'immortal', 'brave', 'electric', 'used', 'worn', 'excellent', 'outstanding', 'graceful', 'anxious', 'mourful', 'due', 'friendly', 'helpful', 'disable', 'magnetize', 'faulty', 'poisonous', 'radioactive', 'windy', 'harmful', 'influential', 'skilled', 'polite', 'beneficial', 'rusty', 'capable', 'competent', 'prejudiced', 'powerful', 'curly', 'gifted', 'dangerous', 'foggy', 'attractive', 'limited', 'valid', 'confident', 'ambitious', 'useful', 'rsponsible', 'sheltered', 'significant', 'strong-minded', 'self-respecting', 'roundabout', 'agreeable', 'foolish', 'silly', 'prelininary', 'primitive', 'nuclear', 'round', 'willing', 'seasick', 'online', 'tentative', 'temporary', 'dirty', 'terrible', 'dreadful', 'entranced', 'precious', 'sincere', 'genuine', 'actual', 'real', 'authentic', 'neat', 'orderly', 'tidy', 'normal', 'proper', 'right', 'accurate', 'political', 'persistent', 'direct', 'outspoken', 'worth', 'worthy', 'worthwhile', 'botanical', 'crucial', 'deadly', 'intellectual', 'medium', 'intermediate', 'hollow', 'neural', 'middle-aged', 'faithful', 'loyal', 'racial', 'numerous', 'heavy', 'repetitive', 'prominent', 'impotant', 'surrounding', 'gradual', 'subjective', 'primary', 'prime', 'major', 'main', 'famous', 'high-handed', 'atom', 'professional', 'exclusive', 'formal', 'magnificent', 'grand', 'ready', 'precise', 'exact', 'eminent', 'automatic', 'proud', 'natural', 'selfish', 'free', 'voluntary', 'antonomous', 'religious', 'stray', 'sufficient', 'ample', 'adequate', 'enough', 'initial', 'utmost', 'maximum', 'minimum', 'supreme', 'best', 'ultimate', 'favourite', 'latest', 'final', 'leading', 'principal', 'left', 'respective', 'elegant', 'aboard', 'out', 'everywhere', 'indeed', "o'clock", 'clumsily', 'straight', 'necessarily', 'not', 'seldom', 'effortlessly', 'regardless', 'ominously', 'shortly', 'soon', 'inevitably', 'impatiently', 'unduly', 'incessantly', 'precariously', 'sadly', 'unfortunately', 'badly', 'radically', 'thoroughly', 'heavily', 'amittedly', 'aloud', 'vertically', 'furthermore', 'moreover', 'hurriedly', 'never', 'ever', 'rudely', 'boldly', 'approximately', 'maybe', 'perhaps', 'loudly', 'around', 'instead', 'certainly', 'aside', 'anyway', 'highly', 'terribly', 'very', 'deeply', 'infinitely', 'respectively', 'sarcastically', 'ironically', 'otherwise', 'emotionally', 'deliberately', 'oddly', 'yet', 'soundly', 'rarely', 'curiously', 'when', 'kindly', 'largely', 'probably', 'afterwards', 'later', 'gaily', 'basically', 'desperately', 'extreme', 'exceedingly', 'almost', 'nearly', 'virtually', 'pratically', 'hardly', 'stoutly', 'simply', 'constructively', 'anxiously', 'further', 'continually', 'solely', 'merely', 'nevertheless', 'discreetly', 'regulay', 'assiduously', 'mentally', 'personally', 'seemingly', 'lavishly', 'possibly', 'positively', 'definitely', 'thirstily', 'fast', 'quickly', 'drily', 'off', 'away', 'immediately', 'twice', 'rashly', 'slowly', 'narrowly', 'guiltily', 'occasionally', 'critically', 'smoothly', 'generally', 'else', 'miraculously', 'violently', 'scornfully', 'gently', 'quietly', 'clearly', 'sentimentally', 'altogether', 'then', 'still', 'ease', 'bitterly', 'even', 'angrily', 'notoriously', 'intensely', 'often', 'actually', 'invariably', 'first', 'anyhow', 'particularly', 'exceptionally', 'early', 'usually', 'normally', 'sympathetically', 'meanwhile', 'likewise', 'abruptly', 'suddenly', 'downstairs', 'sideways', 'why', 'steadily', 'nowhere', 'however', 'faintly', 'apparently', 'obviously', 'evidently', 'now', 'nowadays', 'rather', 'fairly', 'quite', 'conversly', 'apart', 'similarly', 'forward', 'downhill', 'up', 'upwards', 'westward', 'down', 'fortunately', 'rapidly', 'promptly', 'technically', 'either', 'too', 'also', 'neither', 'once', 'partly', 'already', 'somehow', 'ago', 'accidentally', 'thereby', 'hence', 'forever', 'especially', 'sometimes', 'originally', 'again', 'elsewhere', 'abroad', 'outdoors', 'today', 'tonight', 'inside', 'upstairs', 'somewhere', 'where', 'there', 'ahead', 'anywhere', 'downtown', 'indoors', 'overhead', 'overnight', 'together', 'here', 'temporarily', 'how', 'thus', 'sincerely', 'genuinely', 'really', 'truly', 'just', 'properly', 'officially', 'obstinately', 'directly', 'mortally', 'repeatedly', 'pemarily', 'exactly', 'punctually', 'confidently', 'always', 'amply', 'eventually', 'recently', 'lately', 'finally', 'extremely', 'therefore', 'is', 'are', 'nor', 'till', 'since', 'unless', 'but', 'and', 'or', 'if', 'whether', 'although', 'though', 'so', 'whenever', 'because', 'wherever', 'another', 'few', 'second', 'whichever', 'more', 'several', 'less', 'both', 'each', 'which', 'whatever', 'any', 'whose', 'much', 'many', 'such', 'most', 'least', 'every', 'some', 'last', 'all', 'bye', 'goodbye', 'ow', 'sorry', 'hello', 'hi', 'no', 'OK', 'cheers', 'pardon', 'seem', 'weigh', 'must', 'shall', 'will', 'might', 'may', 'can', 'need', 'ought to', 'should', 'capital', 'ladder', 'meantime', 'dozen', 'envy', 'teenager', 'headlight', 'rudder', 'hawser', 'usage', 'campus', 'institution', 'horn', 'mummy', 'instalment', 'bay', 'pole', 'backwater', 'lounge', 'windscreen', 'spire', 'institute', 'regiment', 'dad', 'mum', 'granny', 'grandma', 'grandpa', 'sidewalk', 'genius', 'disability', 'policeman', 'policewoman', 'shawl', 'handbag', 'freedom', 'tissue', 'value', 'clinic', 'orbit', 'shopkeeper', 'wage', 'machinery', 'granddaughter', 'grandchild', 'grandfather', 'grandparent', 'grandmother', 'immigrant', 'tusk', 'schoolboy', 'experience', 'coin', 'motorway', 'college', 'knot', 'hat', 'rim', 'ministry', 'officer', 'stalk', 'gram', 'cleft', 'furniture', 'lap', 'hurry', 'T-shirt', 'X-ray', 'blouse', 'aspirin', 'cancer', 'AIDS', 'attraction', 'arrangement', 'safety', 'security', 'shore', 'punctuality', 'glow', 'ounce', 'ballet', 'handle', 'white', 'daytime', 'percentage', 'percent', 'millionaire', 'class', 'spot', 'zebra', 'porter', 'edition', 'version', 'office', 'semicircle', 'helper', 'favour', 'assistance', 'kidnapper', 'baseball', 'package', 'slice', 'mist', 'jewellery', 'conservation', 'protection', 'bowling', 'conservative', 'Thermos', 'insurance', 'premium', 'guarantee', 'revenge', 'newsagent', 'newspaper', 'journal', 'grievance', 'storm', 'violence', 'popcorn', 'explosion', 'cup', 'sorrow', 'sadness', 'north', 'context', 'vest', 'quilt', 'undergraduate', 'instinct', 'bandage', 'nostril', 'nose', 'dagger', 'comparison', 'ratio', 'pizza', 'competition', 'notebook', 'graduation', 'fireplace', 'boundary', 'edge', 'pad', 'penny', 'variation', 'fickleness', 'debate', 'punctuation', 'label', 'logo', 'title', 'sign', 'standard', 'criterion', 'expression', 'surface', 'indication', 'performance', 'performer', 'bingo', 'ice', 'ice cream', 'iceberg', 'fridge', 'biscuit', 'disease', 'illness', 'virus', 'ward', 'patient', 'glass', 'pineapple', 'neck', 'museum', 'disadvantage', 'variety', 'tragedy', 'shortage', 'layout', 'cloth', 'rifle', 'pace', 'ministry', 'proportion', 'section', 'part', 'department', 'material', 'wealth', 'belongings', 'tailor', 'referee', 'rainbow', 'menu', 'visitor', 'restaurant', 'dining room', 'warehouse', 'playground', 'operator', 'grass', 'meadow', 'draft', 'strawberry', 'lawn', 'sketch', 'toilet', 'measurement', 'test', 'strategy', 'layer', 'fork', 'plug', 'socket', 'tea', 'sauser', 'teapot', 'turning', 'dismay', 'difference', 'output', 'product', 'length', 'overcoat', 'bench', 'giraffe', 'trousers', 'gallery', 'stocking', 'routine', 'excess', 'superman', 'supermarket', 'jibe', 'tide', 'convoy', 'fare', 'workshop', 'garage', 'wheel', 'station', 'wreck', 'composure', 'shirt', 'growth', 'ingredient', 'component', 'composition', 'success', 'accomplishment', 'achievement', 'attainment', 'adult', 'member', 'honesty', 'castle', 'city', 'cruise', 'passenger', 'steward', 'punishment', 'extent', 'procedure', 'orange', 'pond', 'duration', 'size', 'equator', 'wing', 'impulse', 'conflict', 'worship', 'pet', 'pump', 'drawer', 'outlet', 'exit', 'background', 'birth', 'birthplace', 'sale', 'outing', 'advent', 'cab', 'taxi', 'taxi driver', 'kitchen', 'chef', 'cupboard', 'cabinet', 'prescriptiom', 'remedy', 'biography', 'tradition', 'fax', 'ship', 'captain', 'bunch', 'window', 'curtain', 'windowsill', 'bed', 'sheet', 'mattress', 'hammer', 'spring', 'dictionary', 'vocabulary', 'china', 'charity', 'cassette', 'disk', 'magnet', 'clump', 'jungle', 'vinegar', 'clump', 'villager', 'village', 'stock', 'existence', 'being', 'delusion', 'mistake', 'error', 'illusion', 'caller', 'packing', 'intention', 'typewriter', 'typist', 'majority', 'vessel', 'cavern', 'ocean', 'avenue', 'block', 'marble', 'mass', 'bullion', 'mainland', 'continent', 'gate', 'rice', 'atmosphere', 'ambassador', 'embassy', 'pin', 'Atlantic', 'elephant', 'Oceanic', 'media', 'headline', 'nature', 'gangster', 'representative', 'congress', 'behalf', 'agency', 'agent', 'algebra', 'compact', 'strap', 'ribbon', 'loan', 'kangaroo', 'bag', 'word', 'bachelor', 'unit', 'conceal', 'egg', 'cake', 'knife', 'missile', 'navigation', 'island', 'prayer', 'arrival', 'burglar', 'principle', 'straw', 'score', 'lamp', 'lantern', 'lighthouse', 'waiting room', 'grade', 'enemy', 'bottom', 'pedestal', 'floor', 'site', 'place', 'location', 'scene', 'cellar', 'geography', 'ground', 'horizon', 'earth', 'globe', 'area', 'region', 'zone', 'carpet', 'subway', 'map', 'rank', 'basement', 'hell', 'earthquake', 'address', 'empire', 'delivery', 'ceremony', 'dot', 'snack', 'electricty', 'telegram', 'refrigerator', 'battery', 'light', 'bulb', 'shaver', 'telephone', 'phone', 'directory', 'booth', 'power line', 'computer', 'television', 'elevator', 'wire', 'film', 'movie', 'cinema', 'e-mail', 'mink coat', 'eagle', 'sculptor', 'sculpture', 'statue', 'enquiry', 'questionaire', 'sause', 'adjustment', 'modem', 'nail', 'top', 'peak', 'attic', 'deposit', 'lose', 'loss', 'northeast', 'east', 'southeast', 'thing', 'stuff', 'winter', 'holly', 'unrest', 'motivation', 'motive', 'animal', 'zoo', 'hole', 'bullfight', 'matador', 'bean', 'bean curd', 'poison', 'ingenuity', 'solitude', 'independence', 'wheelbarrow', 'reader', 'belly', 'vacation', 'degree', 'ferry', 'shorts', 'pants', 'skirt', 'sock', 'phrase', 'phrasebook', 'paragraph', 'passage', 'pile', 'team', 'queue', 'contrast', 'dialogue', 'opponent', 'ton', 'goose', 'moth', 'child', 'son', 'ear', 'earache', 'dioxde', 'motor', 'publication', 'invention', 'fever', 'occurrence', 'incident', 'frequency', 'discovery', 'spokesman', 'pronunciation', 'development', 'raft', 'judge', 'franc', 'law', 'court', 'translation', 'translator', 'irritation', 'prosperity', 'boom', 'objection', 'feedback', 'raction', 'crime', 'range', 'convenience', 'method', 'way', 'means', 'aspect', 'manner', 'style', 'mode', 'direction', 'defence', 'roof', 'landlord', 'room', 'premises', 'house', 'textile', 'relaxation', 'flight', 'pilot', 'aeroplane', 'airplane', 'plane', 'aiefield', 'Afica', 'fertilizer', 'litter', 'lung', 'fee', 'cent', 'division', 'classification', 'seperation', 'distribution', 'mark', 'analysis', 'minute', 'tomb', 'grave', 'chalk', 'pink', 'powder', 'wind', 'landscape', 'scenery', 'beauty spot', 'fan', 'custom', 'kite', 'maple', 'beehive', 'hive', 'honey', 'volt', 'armchair', 'service', 'waiter', 'costume', 'blessing', 'radiation', 'decay', 'father', 'parent', 'payment', 'load', 'commander', 'appendix', 'copy', 'chorus', 'adaptation', 'refinement', 'improvement', 'correction', 'lid', 'concept', 'liver', 'gratitude', 'feeling', 'sense', 'rugby', 'hay', 'interference', 'steel', 'pen', 'piano', 'pianist', 'harbour', 'port', 'lamb', 'golf', 'mountain', 'freeway', 'please', 'farewell', 'pigeon', 'song', 'opera', 'singer', 'revolution', 'compartment', 'root', 'base', 'evidence', 'factory', 'engineer', 'union', 'tool', 'worker', 'industry', 'salary', 'job', 'schedule', 'businessman', 'busman', 'bus', 'bus stop', 'rooster', 'cock', 'kilometre', 'road', 'highway', 'citizen', 'bull', 'ox', 'justice', 'formula', 'company', 'corporation', 'enterprise', 'flat', 'apartment', 'park', 'limelight', 'pricess', 'efficiency', 'archway', 'arch', 'communism', 'communist', 'republic', 'supply', 'hook', 'dog', 'purchase', 'shopping', 'estimate', 'aunt', 'clavichord', 'eccentricity', 'grain', 'cor n', 'skeleton', 'bone', 'drum', 'encouragement', 'story', 'tale', 'plot', 'customer', 'consultant', 'employee', 'employer', 'melon', 'widow', 'monster', 'devotion', 'connection', 'relationship', 'relation', 'bearing', 'observation', 'outlook', 'sightseeing', 'audience', 'tube', 'pipe', 'administration', 'irrigation', 'bush', 'tin', 'jar', 'ray', 'announcer', 'advertisement', 'advertiser', 'tortoise', 'regularity', 'scale', 'regulation', 'rule', 'trick', 'ghost', 'counter', 'aristocrat', 'lord', 'pot', 'nationality', 'chess', 'nation', 'country', 'border', 'frontier', 'jelly', 'jam', 'pie', 'juice', 'progress', 'fault', 'surplus', 'sea', 'coast', 'seashore', 'altitude', 'seashell', 'seashore', 'seaweed', 'pirate', 'customs', 'navy', 'seagull', 'sea level', 'beach', 'gulf', 'strait', 'channel', 'pest', 'fear', 'implication', 'chill', 'hamburger', 'sweat', 'action', 'march', 'baggage', 'luggage', 'pedestrian', 'behavior', 'deed', 'planet', 'profession', 'voyage', 'airline', 'aircraft', 'spacecraft', 'terminal', 'millimetre', 'curiosity', 'luck', 'number', 'choir', 'contract', 'breeze', 'peace', 'river', 'core', 'walnut', 'box', 'jaw', 'darkness', 'blackboard', 'blackberry', 'black', 'trail', 'bomber', 'red', 'flood', 'marquis', 'monkey', 'back', 'rear', 'heel', 'result', 'chunk', 'candidate', 'breath', 'fox', 'pepper', 'carrot', 'beard', 'lake', 'butterfly', 'Internet', 'barbecue', 'nurse', 'passport', 'flower', 'bloom', 'vase', 'wreath', 'garden', 'skateboard', 'comedian', 'slide', 'skier', 'chemistry', 'cosmetic', 'draw', 'painter', 'topic', 'suspicion', 'ankle', 'mirth', 'circuit', 'environment', 'surroundings', 'fantasy', 'emperor', 'wasp', 'dusk', 'gold', 'yellow', 'butter', 'ash', 'plaster', 'grey', 'recovery', 'response', 'echo', 'accountant', 'meeting', 'conference', 'chamber', 'painting', 'wedding', 'mixture', 'concoction', 'compound', 'chaos', 'activity', 'movement', 'fire', 'match', 'train', 'spark', 'turkey', 'rocket', 'volcano', 'ham', 'Mars', 'flame', 'blaze', 'van', 'stall', 'cargo', 'goods', 'acquisition', 'invitation', 'winner', 'stroke', 'hunger', 'starvation', 'airport', 'chance', 'fortune', 'opportunity', 'machnie', 'robot', 'mechanic', 'muscle', 'chicken', 'grudge', 'basis', 'foundation', 'fund', 'exciting', 'laser', 'passion', 'jeep', 'guitar', 'torrent', 'sickness', 'assembly', 'dormitory', 'geometry', 'scheme', 'programme', 'calculator', 'note', 'diary', 'memory', 'reporter', 'record holder', 'discipline', 'monument', 'souvenir', 'skill', 'technician', 'technique', 'season', 'silence', 'addition', 'gallon', 'clamp', 'jacket', 'home', 'fellow', 'guy', 'tutor', 'housewife', 'homework', 'housework', 'hometown', 'deck', 'beetle', 'holiday', 'assumption', 'price', 'driving licence', 'shelf', 'tip', 'nut', 'spy', 'interval', 'shoulder', 'hardship', 'lookout', 'prison', 'gaoler', 'decline', 'scissors', 'review', 'inspection', 'inspector', 'hut', 'establishment', 'proposal', 'suggestion', 'suggest', 'advice', 'construction', 'architect', 'building', 'architecture', 'sword', 'health', 'gym', 'fleet', 'identification', 'keyboard', 'arrow', 'future', 'lecture', 'bonus', 'reward', 'prize', 'award', 'scholarship', 'medal', 'rainfall', 'communication', 'traffic', 'vehicle', 'symphony', 'dealer', 'sunurb', 'tape', 'glue', 'coach', 'vicar', 'teacher', 'classroom', 'professor', 'church', 'education', 'educate', 'educator', 'angle', 'corner', 'role', 'winch', 'dumpling', 'foot', 'footstep', 'toe', 'car', 'festical', 'saving', 'rhythm', 'phase', 'reception', 'receptionist', 'attendant', 'receiver', 'street', 'neighbourhood', 'masterpiece', 'structure', 'consequence', 'outcome', 'effect', 'combination', 'marriage', 'conclusion', 'ending', 'end', 'sister', 'liberation', 'solution', 'interpretation', 'explanation', 'mustard', 'credit', 'debt', 'amount', 'metal', 'Venus', 'treasure', 'pyramid', 'allowance', 'grip', 'tension', 'caution', 'tournament', 'progress', 'evolution', 'import', 'entry', 'economy', 'director', 'manager', 'management', 'panic', 'terror', 'surprise', 'fright', 'thirller', 'spectacle', 'energy', 'delicacy', 'spirit', 'wheal', 'alarm', 'constable', 'police', 'race', 'rival', 'competitor', 'mirror', 'dilemma', 'drought', 'alcohol', 'wine', 'pub', 'ambulance', 'lifeboat', 'dweller', 'inhabitant', 'resident', 'bow', 'bureau', 'rectangle', 'sentence', 'immensity', 'triumph', 'impact', 'giant', 'boulder', 'club', 'theatre', 'distance', 'hurricane', 'saw', 'zigzag', 'party', 'contribution', 'roll', 'cabbage', 'decision', 'determination', 'resolution', 'despair', 'jazz', 'troop', 'king', 'county', 'coffee', 'café', 'truck', 'lorry', 'card', 'opening', 'switch', 'outset', 'beginning', 'expense', 'view', 'guard', 'archaeologist', 'exam', 'trial', 'grill', 'oven', 'technology', 'subject', 'science', 'scientist', 'chin', 'particle', 'shell', 'carriage', 'cocoa', 'Coke', 'possibility', 'prospect', 'videophone', 'guest', 'living room', 'textbook', 'pleading', 'space', 'air', 'air hostess', 'airmail', 'dinosaur', 'accusation', 'thirst', 'dictation', 'gum', 'interpreter', 'accent', 'span', 'bar', 'delight', 'happiness', 'speedboat', 'chopstick', 'width', 'breadth', 'relief', 'mania', 'rapture', 'truant', 'moor', 'mineral', 'framework', 'frame', 'insect', 'confusion', 'trouble', 'extension', 'expansion', 'rubbish', 'garbage', 'litter basket', 'dustman', 'dustbin', 'zipper', 'zip', 'wax', 'crayon', 'candle', 'correspondence', 'shuttle', 'source', 'blue', 'basketball', 'basket', 'cable', 'wolf', 'labour', 'labourer', 'boss', 'tiger', 'mouse', 'rat', 'pancake', 'band', 'instrument', 'fun', 'thunder', 'radar', 'thunderstorm', 'radium', 'centimetre', 'pear', 'divorce', 'departure', 'dawn', 'cockcrow', 'present', 'gift', 'listeria', 'milometre', 'haircut', 'barbershop', 'barber', 'hairdresser', 'understanding', 'comprehension', 'wit', 'history', 'historian', 'cube', 'stereo', 'profit', 'exception', 'example', 'instance', 'conjunction', 'succession', 'dress', 'league', 'contact', 'face', 'exercise', 'chain', 'conscience', 'couple', 'fortnight', 'procession', 'liquor', 'hunter', 'fissure', 'flaw', 'gap', 'neighbour', 'soul', 'ring', 'tie', 'leadership', 'leader', 'airspace', 'territory', 'realm', 'flow', 'flu', 'fashion', 'tramp', 'fluency', 'dragon', 'lobster', 'cage', 'storey', 'stair', 'stove', 'cooker', 'land', 'army', 'video', 'tape recorder', 'recorder', 'studio', 'deer', 'lamp post', 'passer-by', 'route', 'tyre', 'screw', 'camel', 'donkey', 'brigade', 'hotel', 'trip', 'journey', 'tour', 'traveller', 'tourism', 'tourist', 'aluminium', 'lawer', 'attorney', 'green', 'sack', 'sparrow', 'measles', 'horse', 'marathon', 'horsepower', 'polo', 'circus', 'ant', 'step', 'microphone', 'pulse', 'satisfaction', 'rambler', 'cartoon', 'cat', 'owl', 'towel', 'fur', 'sweater', 'spear', 'contradiction', 'anchor', 'adventure', 'trade', 'commerce', 'cap', 'rose', 'coal', 'virtue', 'beauty', 'art', 'puma', 'fascination', 'door', 'latch', 'hall', 'dash', 'mammoth', 'labyrinth', 'bewilderment', 'riddle', 'metre', 'secretary', 'code', 'bee', 'cottom', 'bread', 'bakery', 'baker', 'flour', 'exposure', 'interview', 'noodle', 'mask', 'description', 'temple', 'fire extingguisher', 'contempt', 'survey', 'demorcracy', 'reputation', 'fame', 'name', 'tomorrow', 'postcard', 'command', 'fate', 'nonsense', 'friction', 'skyscraper', 'motorcycle', 'sharpener', 'mushroom', 'magic', 'devil', 'rag', 'stranger', 'ink', 'obscurity', 'occasion', 'hen', 'mother', 'thumb', 'board', 'plank', 'carpenter', 'puppet', 'wood', 'Jupiter', 'target', 'aim', 'witness', 'catalogue', 'shower', 'pasture', 'taxpayer', 'milk', 'cheese', 'cow', 'cream', 'boy', 'south', 'Antarctic', 'difficulty', 'problem', 'brain', 'interior', 'content', 'underclothes', 'underwear', 'ability', 'power', 'competence', 'nylon', 'mud', 'year', 'age', 'clay', 'bird', 'nest', 'birdcage', 'lemon', 'lemonade', 'cattle', 'dairy', 'steak', 'beef', 'jeans', 'bond', 'button', 'farm', 'famer', 'peasant', 'agriculture', 'slavery', 'endeavour', 'anger', 'salesgirl', 'daughter', 'waitress', 'girl', 'maid', 'woman', 'stewardess', 'lady', 'queen', 'actress', 'heroine', 'maidservant', 'hostess', 'Europe', 'gear', 'volleyball', 'drainage', 'dish', 'plate', 'judgement', 'course', 'jet', 'fountain', 'basin', 'cuisine', 'recipe', 'friend', 'mate', 'shed', 'collision', 'criticism', 'skin', 'leather', 'wallet', 'beer', 'brewery', 'temper', 'preference', 'prejudice', 'moment', 'hoax', 'ticket', 'parquet', 'puzzle', 'jigsaw', 'spelling', 'poverty', 'brand', 'pint', 'character', 'ping-pong', 'equality', 'pan', 'bungalow', 'balance', 'lull', 'civilian', 'plain', 'assessment', 'comment', 'critic', 'apple', 'screen', 'bottle', 'destruction', 'grape', 'popularity', 'waterfall', 'wife', 'deception', 'miracle', 'discrimination', 'cyclist', 'flag', 'beggar', 'sitting  room', 'origin', 'crane', 'climate', 'effort', 'bubble', 'ballon', 'gas', 'steamship', 'petrol', 'organ', 'kilo', 'pencil', 'signature', 'visa', 'forehead', 'front', 'predecessor', 'preface', 'eve', 'prelude', 'money', 'purse', 'dever', 'submarine', 'gun', 'emphasis', 'wall', 'spade', 'bridge', 'coincidence', 'chocolate', 'cliff', 'eggplant', 'darling', 'intruder', 'bedding', 'adolescence', 'youth', 'adolescent', 'frog', 'hypnotize', 'scorn', 'cleaner', 'emotion', 'situation', 'mood', 'celebration', 'dome', 'autumn', 'swing', 'prisoner', 'ball', 'bat', 'goal', 'sphere', 'doorknob', 'distinction', 'district', 'tendency', 'trend', 'tune', 'cookie', 'enclosure', 'curriculum', 'crew', 'personnel', 'staff', 'authority', 'fist', 'boxing', 'boxer', 'drawback', 'shortcoming', 'defect', 'lack', 'absence', 'freckle', 'magpie', 'fuel', 'heat', 'hot dog', 'enthusiasm', 'enthusiant', 'person', 'man', 'people', 'human', 'abortion', 'pavement', 'population', 'mankind', 'folk', 'crowd', 'satellite', 'mercy', 'kindness', 'recognition', 'task', 'diet', 'daylight', 'calendar', 'date', 'wool', 'glory', 'volume', 'capacity', 'container', 'capsule', 'ease', 'harmony', 'meat', 'flesh', 'mince', 'worm', 'breast', 'entrance', 'invasion', 'software', 'weakness', 'mumps', 'racing', 'triangle', 'tricycle', 'sandwich', ' paratrooper', 'broom', 'forest', 'monk', 'pestiside', 'sardine', 'sofa', 'salmonella', 'sand', 'shark', 'fool', 'cave', 'goat', 'fence', 'coral', 'lightning', 'scar', 'harm', 'injury', 'wound', 'shop', 'store', 'firm', 'commodiy', 'commercialization', 'merchant', 'business', 'moustache', 'god', 'scoop', 'spoon', 'minority', 'whistle', 'luxury', 'tongue', 'snake', 'equipment', 'facility', 'society', 'socialism', 'socialist', 'community', 'shot', 'photographer', 'application', 'applicant', 'identity', 'status', 'height', 'body', 'gentleman', 'pit', 'depth', 'chasm', 'foresight', 'priest', 'myth', 'nerve', 'mystery', 'litre', 'production', 'manufacturer', 'survival', 'life', 'birthday', 'ecology', 'creature', 'biochemistry', 'biology', 'sound', 'rope', 'province', 'chant', 'victory', 'feast', 'failure', 'undoing', 'unemployment', 'disappearance', 'poem', 'poetry', 'poet', 'lion', 'fresco', 'decade', 'crossing', 'crossing', 'limestone', 'stalagmite', 'stone', 'oil', 'era', 'time', 'timetable', 'practice', 'experiment', 'lab', 'groceries', 'grocer', 'canteen', 'food', 'appetite', 'mission', 'user', 'soldier', 'century', 'world', 'mayor', 'market', 'accident', 'affair', 'matter', 'snob', 'sight', 'eyesight', 'vision', 'definition', 'collection', 'harvest', 'receipt', 'income', 'radio', 'hand', 'arm', 'watch', 'flashlight', 'torch', 'torchlight', 'handkerchief', 'gesture', 'operation', 'glove', 'suitcase', 'cart', 'wrist', 'craft', 'palm', 'finger', 'fingernail', 'victim', 'beast', 'salesman', 'shop assistant', 'conductor', 'book', 'schoolbag', 'bookshop', 'bookcase', 'handwritting', 'writing paper', 'desk', 'uncle', 'dressing table', 'comb', 'negligence', 'comfort', 'vegetable', 'salad', 'greengrocer', 'ransom', 'acquaintance', 'tree', 'koala', 'trunk', 'branch', 'resin', 'data', 'database', 'quantity', 'mathematics', 'figure', 'brush', 'downfall', 'twin', 'binoculars', 'frost', 'water', 'dam', 'fruit', 'kettle', 'crytal', 'reservoir', 'waterspout', 'tap', 'level', 'sailor', 'seaman', 'steam', 'tax', 'sleeping bag', 'sleeper', 'order', 'statement', 'caption', 'silk', 'velvet', 'driver', 'logic', 'thinking', 'death', 'squirrel', 'pine', 'milkman', 'ambition', 'vegeterian', 'speed', 'hostel', 'plastic', 'yogurt', 'garlic', 'arithmetic', 'fragment', 'rubble', 'tunnel', 'grandson', 'damage', 'requirement', 'ownership', 'index', 'detail', 'tower', 'pedal', 'typhoon', 'madam', 'sun', 'perspective', 'attitude', 'conversation', 'remark', 'blanket', 'explorer', 'carbon', 'soup', 'cousin', 'sugar', 'candy', 'sweet', 'praying mantis', 'peach', 'crockery', 'discussion', 'nuisance', 'suite', 'juncture', 'feature', 'privilege', 'characteristic', 'pain', 'reference', 'hint', 'recommendation', 'gymnastics', 'strength', 'system', 'PE ', 'stadium', 'sport', 'razor', 'talent', 'faculty', 'ceiling', 'sky', 'weather', 'heaven', 'paradise', 'obseratory', 'astronomy', 'astronomer', 'field', 'dessert', 'provocation', 'challenge', 'circumstance', 'treaty', 'iron', 'rail', 'railway', 'hearing', 'parking', 'access', 'ventilation', 'currency', 'macaroni', 'classmate', 'partner', 'companion', 'peer', 'sympathy', 'colleague', 'consent', 'copper', 'childhood', 'statistic', 'bucket', 'suffering', 'misery', 'theft', 'hair', 'helmet', 'mind', 'input', 'investment', 'pattern', 'illustration', 'chart', 'graph', 'picture', 'diagram', 'library', 'librarian', 'emergency', 'breakthrough', 'raid', 'butcher', 'potato', 'dialect', 'soil', 'toast', 'rabbit', 'unity', 'sales  rep', 'leg', 'hip', 'mop', 'tractor', 'doll', 'apperance', 'exterior', 'foreigner', 'surgery', 'surgeon', 'coat', 'pea', 'toy', 'supper', 'evening', 'bowl', 'dynasty', 'palace', 'crown', 'kingdom', 'prince', 'web', 'net', 'network', 'tennis', 'website', 'telescope', 'crisis', 'danger', 'risk', 'pitfall', 'whisky', 'threat', 'microwwave', 'scarf', 'apron', 'dimension', 'vitamin', 'tail', 'client', 'committee', 'commission', 'sake', 'fiance', 'position', 'flavour', 'stomach', 'stomach ache', 'temperature', 'warmth', 'culture', 'file ', 'document', 'stationery', 'pencil case', 'stationer', 'civilization', 'diploma', 'paperwork', 'literature', 'article', 'essay', 'mosquito', 'stability', 'greeting', 'purpose', 'lettuce', 'snail', 'bedroom', 'stain', 'blot', 'pollution', 'dirt', 'junk', 'ignorance', 'innocence', 'quintuplet', 'lunch', 'midnight', 'force', 'weapon', 'stage', 'physics', 'physicist', 'substance', 'owner', 'fog', 'west', 'northwest', 'watermelon', 'tomato', 'southwest', 'smoker', 'valley', 'stream', 'knee', 'habit', 'convention', 'idiom', 'shampoo', 'washroom', 'laundry', 'bath', 'affection', 'comedy', 'drama', 'cell', 'bacteria', 'string', 'underside', 'afternoon', 'summer', 'pioneer', 'sir', 'fibre', 'leisure', 'bacon', 'revulsion', 'monitor', 'microscope', 'cash', 'reality', 'fact', 'phenomenon', 'line', 'thread', 'clue', 'limit', 'limitation', 'restriction', 'consititution', 'trap', 'lodge', 'countryside', 'album', 'interaction', 'resemblance', 'faith', 'champagne', 'sausage', 'banana', 'perfume', 'cigarette', 'soap', 'tank', 'case', 'thought', 'imagination', 'necklace', 'project', 'item', 'ivory', 'symbol', 'eraser', 'rubber', 'fireman', 'consumer', 'recreation', 'message', 'parcel', 'packet', 'fraction', 'quiz', 'boat', 'mat', 'rug', 'kid', 'trumpet', 'alley', 'Miss', 'inn', 'path', 'wheat', 'kitten', 'patch', 'hill', 'hour', 'novel', 'fiction', 'novelist', 'violin', 'dinghy', 'cottage', 'cabin', 'minibus', 'pupil', 'portrait', 'headmaster', 'schoolmate', 'laugh', 'association', 'teamwork', 'settlement', 'shoe', 'psychology', 'heart', 'appreciation', 'newly-wed', 'bridegroom', 'bride', 'novice', 'news', 'journalist', 'bulletin', 'letter', 'envelope', 'signal', 'information', 'belief', 'confidence', 'interest', 'week', 'galaxy', 'star', 'image', 'shape', 'model', 'survivor', 'welfare', 'sex', 'brother', 'chest', 'bear', 'panda', 'rest', 'revision', 'shame', 'sleeve', 'licence', 'commitment', 'noise', 'election', 'vote', 'option', 'boot', 'term', 'term', 'kindergarten', 'student', 'theory', 'study', 'learner', 'school', 'scholar', 'snow', 'cigar', 'snowman', 'cod', 'caveman', 'blood', 'cruiser', 'training', 'pressure', 'stress', 'rhyme', 'duck', 'tooth', 'toothpaste', 'toothbrush', 'toothache', 'dentist', 'aphid', 'Asia', 'throat', 'smoke', 'chimney', 'ashtray', 'firework', 'smog', 'tobacco', 'delay', 'rock', 'seminar', 'salt', 'colour', 'eye', 'tear', 'speaker', 'speech', 'actor', 'disgust', 'boredom', 'saying', 'sheep', 'mutton', 'sunshine', 'sunlight', 'balcony', 'onion', 'pension', 'oxygen', 'sample', 'specimen', 'waist', 'belt', 'rumour', 'drug', 'herb', 'chemist', 'tablet', 'pill', 'medicine', 'demand', 'element', 'key', 'margin', 'picnic', 'wildlife', 'hobby', 'leaf', 'page', 'night', 'liquid', 'handful', 'half', 'gang', 'side', 'teaspoonful', 'swarm', 'horde', 'generation', 'bit', 'stack', 'period', 'while', 'heap', 'meal', 'household', 'session', 'lesson', 'quarter', 'list', 'glimpse', 'spoonful', 'lifetime', 'pair', 'suit', 'day', 'loaf', 'series', 'sequence', 'gust', 'consensus', 'clothes', 'clothing', 'pocket', 'wardrobe', 'collar', 'cloakroom', 'doctor', 'physician', 'hospital', 'dashboard', 'immigration', 'settler', 'pity', 'remains', 'doubt', 'chair', 'fete', 'artiste', 'artist', 'agenda', 'parliament', 'anecdote', 'opinion', 'disagreement', 'purpose', 'meaning', 'factor', 'shade', 'syllable', 'music', 'concert', 'musician', 'silver', 'bank', 'silverware', 'introduction', 'reminder', 'engine', 'quotation', 'recluse', 'privacy', 'impression', 'seal', 'pound', 'inch', 'mile', 'acre', 'soccer', 'hero', 'baby', 'infant', 'cherry', 'porrot', 'eagle eye', 'camp', 'campfire', 'nutrition', 'influence', 'shadow', 'cardboard', 'possession', 'bravey', 'courage', 'instructon', 'ware', 'servant', 'benefit', 'advantage', 'priority', 'anxiety', 'humor', 'post', 'mail', 'postman', 'liner', 'stamp', 'mailbox', 'postcode', 'postage', 'tanker', 'pastry', 'oilfield', 'chip', 'grease', 'parade', 'nomad', 'game', 'player', 'pool', 'swimming', 'swimmer', 'friendship', 'tram', 'nursery', 'temptation', 'fish', 'torpedo', 'entertainment', 'fisherman', 'joy', 'exhilaration', 'amusement', 'astronaut', 'universe', 'spaceship', 'feather', 'badminton', 'rain', 'umbrella', 'raincoat', 'grammar', 'tone', 'language', 'bathtub', 'bathroom', 'forecast', 'precaution', 'expectation', 'budget', 'preview', 'reservation', 'dollar', 'gardening', 'log', 'reason', 'atom', 'circle', 'excursion', 'yard', 'courtyard', 'desire', 'appointment', 'month', 'moonlight', 'moon', 'reading', 'cloud', 'motion', 'campaign', 'sneaker', 'athlete', 'canal', 'transport', 'carrier', 'transportation', 'weed', 'handyman', 'disorder', 'mess', 'magazine', 'catastrophe', 'disaster', 'grower', 'consideration', 'in', 'suspension', 'approval', 'praise', 'sponser', 'funeral', 'breakfast', 'morning', 'brunch', 'voice', 'duty', 'responsibliity', 'thief', 'bomb', 'explosive', 'exhibition', 'presentation', 'battle', 'war', 'platform', 'peiece', 'chapter', 'octopus', 'husband', 'tent', 'bill', 'account', 'barrier', 'obstacle', 'poster', 'claw', 'paw', 'care', 'photo', 'photograph', 'camera', 'shelter', 'discount', 'philosopher', 'philosopher', 'needle', 'detective', 'rarity', 'vacuum', 'truth', 'pineapple', 'town', 'vibration', 'horror', 'argument', 'contention', 'dispute', 'conquest', 'dinner', 'square', 'text', 'noon', 'proof', 'certificate', 'policy', 'government', 'ombudsman', 'politics', 'statesman', 'politician', 'symptom', 'cheque', 'knowledge', 'spider', 'niece', 'nephew', 'ruler', 'helicopter', 'career', 'employment', 'occupation', 'prizefighter', 'clerk', 'plant', 'botany', 'colony', 'paper', 'guidance', 'guide', 'compass', 'fingerprint', 'volunteer', 'uniform', 'treatment', 'quality', 'wisdom', 'intelligence', 'middle', 'central', 'destination', 'bell', 'clock', 'stalactite', 'category', 'sort', 'seed', 'burden', 'repetition', 'gravity', 'weight', 'importance', 'milestone', 'event', 'significance', 'issue', 'weekday', 'weekend', 'anniversary', 'vicinity', 'porridge', 'elbow', 'curse', 'wrinkle', 'jewellery', 'pig', 'pork', 'bamboo', 'editor', 'mainframe', 'examiner', 'host', 'theme', 'chairman', 'idea', 'accommodation', 'injection', 'notice', 'attention', 'storage', 'column', 'congratulation', 'specialist', 'expert', 'academy', 'patent', 'concentration', 'brick', 'diversion', 'crop', 'decoration', 'device', 'state', 'condition', 'preparation', 'accuracy', 'permission', 'admission', 'table', 'qualification', 'finance', 'brochure', 'resource', 'bullet', 'purple', 'alphabet', 'bicycle', 'bike', 'cycle', 'pride', 'self', 'self-discipline', 'self-improvement', 'liberty', 'buffet', 'cafeteria', 'religion', 'brown', 'summary', 'sum', 'total', 'format', 'president', 'corridor', 'smuggler', 'track', 'football', 'group', 'formation', 'organization', 'motherland', 'howmland', 'ancestor', 'diamond', 'oil rig', 'mouth', 'lip', 'speed limit', 'deadline', 'offender', 'vice', 'offence', 'drunk', 'honour', 'dignity', 'yesterday', 'author', 'writer', 'function', 'cushion', 'seat', 'motto', 'hundred', 'thousand', 'billion', 'million', 'table tennis', 'anyone', 'underneath', 'below', 'through', 'behind', 'than', 'until', 'of', 'unlike', 'except', 'besides', 'from', 'to', 'versus', 'throughout', 'for', 'about', 'with', 'acorss', 'despite', 'plus', 'minus', 'into', 'via', 'astride', 'without', 'per', 'mine', 'onto', 'towards ', 'as', 'by', 'against', 'beyond', 'between', 'at', 'above', 'after', 'beside', 'during', 'upon', 'beneath', 'under', 'before', 'among', 'on', 'opposite', 'near', 'alongside', 'over', 'outside', 'within', 'along', 'lot', 'that', 'those', 'what', 'this', 'these', 'plenty', 'nobody', 'nothing', 'none', 'everybody', 'everyone', 'somebody', 'someone', 'something', 'anybody', 'anything', 'who', 'whom', 'everything', 'welcome', 'ski', 'run', 'react', 'haunt', 'marry', 'erupt', 'twitter', 'toss', 'rattle', 'mix', 'tire', 'break', 'rust', 'form', 'fuse', 'snap', 'scream', 'haul', 'accord', 'am', 'mourn', 'starve', 'love', 'dispose', 'arrange', 'console', 'install', 'press', 'imply', 'wade', 'hide', 'dedicate', 'attach', 'treat', 'lower', 'blame', 'attribute', 'impose', 'regard', 'wag', 'rid', 'move', 'stumble', 'aid', 'assist', 'help', 'wrap', 'include', 'involve', 'contain', 'comprise', 'surrounding', 'peel', 'keep', 'remain', 'preserve', 'safeguard', 'protect', 'report', 'clutch', 'complain', 'expose', 'explode', 'burst', 'recite', 'fumble', 'jump', 'compare', 'despise', 'graduate', 'acvoid', 'compile', 'fade', 'blacken', 'loosen', 'express', 'convey', 'indicate', 'behave', 'performant', 'dial', 'pull', 'broadcast', 'sow', 'exclude', 'disregard', 'disagree', 'differ', 'dislike', 'dismiss', 'object', 'furnish', 'walk', 'wipe', 'polish', 'scrub', 'guess', 'visit', 'participate', 'attend', 'join', 'compete', 'measure', 'insert', 'ascertain', 'perceive', 'brake', 'dismantle', 'generate', 'shiver', 'tremble', 'sing', 'exceed', 'overtake', 'taunt', 'sneer', 'wild', 'desplay', 'success', 'become', 'motivate', 'undertake', 'promise', 'admit', 'acknowledge', 'multiply', 'punish', 'clairfy', 'eat', 'fill', 'rush', 'sniff', 'publish', 'bid', 'export', 'betray', 'born', 'show', 'sell', 'emerge', 'execute', 'deal', 'touch', 'penetrate', 'cross', 'wear', 'spread', 'infect', 'transmit', 'deliver', 'gasp', 'found', 'create', 'blow', 'sob', 'resign', 'magnetize', 'sting', 'unpack', 'stimulate', 'promote', 'destroy', 'survive', 'exist', 'consist', 'achieve', 'beat', 'call', 'yawn', 'snore', 'undo', 'hunt', 'disturb', 'pester', 'bother', 'interrupt', 'smash', 'print', 'type', 'manufacture', 'represent', 'replace', 'substitute', 'bring', 'lead', 'arrest', 'worry', 'dust', 'rebound', 'bounce', 'rewind', 'reach', 'arrive', 'apologize', 'derive', 'offend', 'advertise', 'wait', 'underetimate', 'drip', 'resist', 'nod', 'carve', 'investigate', 'adjust', 'modify', 'settle', 'subscribe', 'dump', 'discard', 'understand', 'amuse', 'mumble', 'read', 'clog', 'conclude', 'hypnotize', 'urge', 'whisper', 'emit', 'tick', 'click', 'chug', 'blare', 'quake', 'invent', 'devise', 'launch', 'happen', 'occur', 'arise', 'swear', 'send', 'gleam', 'detect', 'discover', 'trace', 'pronounce', 'develop', 'capsize', 'translate', 'flourish', 'contracdict', 'oppose', 'protest', 'reflect', 'return', 'commit', 'defend', 'set', 'relax', 'put', 'indulge', 'fly', 'dread', 'bark', 'abolish', 'divide', 'split', 'classify', 'assign', 'distribute', 'allocate', 'analyse', 'sew', 'deny', 'hatch', 'obey', 'serve', 'capture', 'float', 'correspond', 'rot', 'pay', 'afford', 'retell', 'reproduce', 'cover', 'alter', 'change', 'reform', 'improve', 'correct', 'outline', 'dare', 'venture', 'feel', 'thank', 'interfere', 'tell', 'isolate', 'dye', 'give', 'prescribe', 'impress', 'define', 'render', 'mete', 'follow', 'plough', 'cultivate', 'prefer', 'industrialize', 'work', 'assail', 'share', 'confess', 'communication', 'evaluate', 'encourage', 'applaud', 'employ', 'shave', 'register', 'shut', 'close', 'observe', 'overfish', 'shout', 'act', 'sail', 'howl', 'drink', 'cooperate', 'verify', 'bake', 'retreat', 'exclaim', 'breathe', 'neglect', 'ignore', 'overlook', 'spend', 'cost', 'row', 'skate', 'slip', 'suspect', 'cheer', 'rouse', 'wave', 'answer', 'reply', 'respond', 'recyle', 'ruin', 'blend', 'gain', 'attain', 'acquire', 'get', 'obtain', 'hit', 'defeat', 'accumulate', 'amass', 'inspire', 'arouse', 'pass', 'soar', 'assemble', 'focus', 'squeeze', 'calculate', 'remember', 'record', 'rcall', 'inherit', 'continue', 'proceed', 'illustrate', 'quicker', 'reinforce', 'strengthen', 'accelerate', 'presume', 'assume', 'disguise', 'pretend', 'steer', 'drive', 'insist', 'imprison', 'subtract', 'diminish', 'decrease', 'reduce', 'examine', 'inspect', 'check', 'prosecute', 'erect', 'establish', 'propose', 'construct', 'build', 'speak', 'swap', 'exchange', 'teach', 'civilize', 'simulate', 'connect', 'receive', 'accept', 'falter', 'freeze', 'combine', 'finish', 'relieve', 'liberate', 'solve', 'resolve', 'explain', 'introduce', 'borrow', 'lend', 'enter', 'submerge', 'forbid', 'prohibit', 'undergo', 'scare', 'refine', 'master', 'plan', 'salute', 'live', 'chew', 'refuse', 'boycott', 'repel', 'specify', 'muster', 'gather', 'concentrate', 'donate', 'contribute', 'curl', 'decide', 'determine', 'open', 'begin', 'start', 'joke', 'explore', 'look', 'see', 'resemble', 'recover', 'heal', 'remonstrate', 'approach', 'cough', 'overcome', 'clone', 'beg', 'intimidate', 'accuse', 'govern', 'control', 'dictate', 'cry', 'whine', 'weep', 'exaggerate', 'spin', 'zoom', 'bind', 'enlarge', 'expand', 'stretch', 'come', 'abuse', 'waste', 'nag', 'leave', 'quit', 'depart', 'exploit', 'utilize', 'link', 'unite', 'relate', 'associate', 'chat', 'clutter', 'scan', 'bleed', 'leak', 'fall', 'drop', 'travel', 'skim', 'bury', 'lurk', 'buy', 'jog', 'straggle', 'pouce', 'bang', 'thrust', 'squint', 'compesate', 'conspire', 'hitchhike', 'depict', 'describe', 'ban', 'imitate', 'grind', 'murder', 'carry', 'hold', 'fetch', 'take', 'overwhelm', 'scratch', 'spoil', 'condense', 'gaze', 'stare', 'pinch', 'unscrew', 'grapple', 'slave', 'attempt', 'glare', 'scramble', 'climb', 'crawl', 'mount', 'clap', 'eliminate', 'drain', 'hobble', 'stagger', 'abandon', 'desert', 'accompany', 'breed', 'spray', 'slam', 'cook', 'swell', 'strike', 'collide', 'crash', 'criticize', 'drift', 'spell', 'taste', 'assess', 'rate', 'crack', 'perch', 'expect', 'hope', 'deceive', 'cheat', 'pray', 'ride', 'plead', 'advance', 'condemn', 'owe', 'emphasize', 'oblige', 'compel', 'enforce', 'rob', 'knock', 'prise', 'cut', 'chop', 'kiss', 'invade', 'pat', 'pour', 'incline', 'bend', 'lean', 'erase', 'celebrate', 'distinguish', 'dispel', 'repel', 'tend', 'qualify', 'cancel', 'tease', 'interpret', 'advise', 'lure', 'locate', 'identify', 'burn', 'let', 'adore', 'endless', 'recognize', 'suppose', 'appoint', 'cast', 'throw', 'tolerate', 'dissolve', 'burgle', 'tuck', 'stroll', 'sweep', 'glance', 'kill', 'omit', 'delete', 'glisten', 'glint', 'flash', 'flicker', 'injure', 'manage', 'design', 'shoot', 'reprimand', 'apply', 'fascinate', 'rise', 'produce', 'grow', 'claim', 'prevail', 'fail', 'overbalance', 'fulfil', 'ripen', 'thrill', 'complicate', 'transform', 'embarrass', 'fix', 'refresh', 'excite', 'simplify', 'perturb', 'exhaust', 'amaze', 'frighten', 'terrify', 'satisfy', 'confuse', 'bewilder', 'annoy', 'enable', 'twist', 'assure', 'disappoint', 'astonish', 'acquaint', 'ventilate', 'plunge', 'dislocate', 'thresh', 'petrify', 'update', 'entile', 'coordinate', 'unsettle', 'convince', 'disillusion', 'depress', 'use', 'occupy', 'calm', 'astound', 'shock', 'try', 'fit', 'adapt', 'release', 'charge', 'collect', 'pack', 'adopt', 'suffer', 'belong', 'count', 'wane', 'wrestle', 'sleep', 'suck', 'say', 'persuade', 'lie', 'think', 'miss', 'rip', 'die', 'scour', 'search', 'resort', 'scurry', 'shrink', 'lock', 'lift', 'collapse', 'talk', 'negotiate', 'sigh', 'evade', 'escape', 'bargain', 'discussion', 'hate', 'ache', 'hurt', 'kick', 'mention', 'refer', 'provide', 'offer', 'cater', 'submit', 'raise', 'warn', 'pick', 'skip', 'dive', 'dance', 'leap', 'listen', 'hear', 'stop', 'stay', 'cease', 'halt', 'inform', 'sympathy', 'agree', 'grant', 'steal', 'insure', 'surrender', 'invest', 'vanish', 'swerve', 'spit', 'push', 'infer', 'rcommend', 'deduce', 'retire', 'devour', 'swallow', 'drag', 'dawdle', 'compromise', 'dig', 'accomplish', 'play', 'save', 'forget', 'threaten', 'smile', 'enclose', 'violate', 'maintain', 'sustain', 'persist', 'tint', 'feed', 'smell', 'greet', 'contaminate', 'pollute', 'mslead', 'misunderstand', 'absorb', 'appeal', 'attract', 'engage', 'wish', 'sacrifice', 'attack', 'wash', 'ransack', 'like', 'fasten', 'disembark', 'sink', 'lay', 'bet', 'descend', 'download', 'appear', 'reveal', 'confine', 'restrict', 'devote', 'correlate', 'believe', 'vary', 'enjoy', 'imagine', 'intend', 'want', 'wonder', 'fancy', 'consume', 'digest', 'disappear', 'sip', 'laugh', 'write', 'unload', 'appreciate', 'trust', 'wake', 'waken', 'restore', 'reconstruct', 'revise', 'mend', 'repair', 'require', 'declare', 'announce', 'suspend', 'hang', 'dangle', 'elect', 'choose', 'select', 'sharpen', 'weaken', 'learn', 'seek', 'inquire', 'ask', 'circulate', 'scold', 'flee', 'crush', 'compress', 'muffle', 'drown', 'extend', 'postpone', 'retrace', 'research', 'invite', 'sway', 'shake', 'bite', 'request', 'snatch', 'depend', 'rely', 'transfer', 'emigrate', 'remove', 'regret', 'realize', 'mean', 'cause', 'quote', 'tempt', 'conceal', 'salvage', 'rescue', 'win', 'affect', 'deserve', 'embrace', 'hug', 'advocate', 'possess', 'boil', 'paddle', 'bathe', 'hesitate', 'fry', 'wander', 'swim', 'have', 'be', 'reserve', 'anticipate', 'foresee', 'predict', 'foretell', 'meet', 'forfive', 'excuse', 'regulate', 'allow', 'permit', 'exert', 'operate', 'consider', 'recur', 'underline', 'engrave', 'paint', 'inscribe', 'puncture', 'pause', 'approve', 'admire', 'extol', 'encounter', 'pose', 'reproach', 'add', 'increase', 'stick', 'paste', 'exhibit', 'conquer', 'fight', 'stand', 'dip', 'entertain', 'find', 'shine', 'fold', 'afflict', 'cherish', 'diagnose', 'vibrate', 'quarrel', 'argue', 'contest', 'demonstrate', 'prove', 'justify', 'confirm', 'earn', 'struggle', 'support', 'dominate', 'know', 'point', 'make', 'cure', 'choke', 'reunite', 'repeat', 'rebuild', 'rediscover', 'resume', 'renew', 'redirect', 'frown', 'evolve', 'preside', 'bless', 'congratulate', 'cling', 'grasp', 'seize', 'catch', 'grab', 'specialize', 'convert', 'relay', 'turn', 'shift', 'equip', 'decorate', 'adorn', 'chase', 'pursue', 'discharge', 'consult', 'boast', 'summarize', 'go', 'hire', 'rent', 'hinder', 'discourage', 'prevent', 'compose', 'constitute', 'organize', 'conduct', 'drill', 'respect', 'waterski', 'sit', 'do', 'prepare', 'dream', 'gesticulate', 'remind', 'interested', 'champion', 'family', 'patience', 'creep', 'please', 'interesting', 'double', 'head', 'headache', 'serious', 'glasses', 'a', 'pleasant', 'pleasantly', 'instruct', 'the', 'assistant']
def find_perfect_number(start_number:int=1,number_to :int= 6,include_number_to:bool=True) -> list[int]:
    back_list=[]
    if number_to>=6:
        try_number=start_number
        while (2**try_number-1)*(2**(try_number-1))<=(number_to if include_number_to else number_to-1):
            if is_prime(2**try_number-1):
                back_list.append((2**try_number-1)*(2**(try_number-1)))
            try_number+=1
        return back_list
    else:
        return []
def is_perfect_number(number:int=None) -> bool:
    sums=0
    for ij in find_factor(number):
        if ij!=number:
            sums+=ij
    if sums==number:
        return True
    return False
def Fibonacci(number:int) -> int:
    if number==1 or number==2:
        return 1
    else:
        return Fibonacci(number-1)+Fibonacci(number-2)
def is_Fibonacci(number:int,return_digit:bool=False) -> (bool|list[bool,int]):
    i=1
    while Fibonacci(i)<=number:
        if Fibonacci(i)==number:
            return True if (not return_digit) else [True,i]
        i+=1
    return False
def permutation(item:Iterable[str]):
    if len(item)==1:
        return [item]
    res=[]
    for i,x in enumerate(item):
        n=item[:i]+item[i+1:]
        for y in permutation(n):
            res.append(x+y)
    return list(set(res))
if __name__=='__main__':
    print(is_Fibonacci(13))
    print(permutation('1145141919810'))