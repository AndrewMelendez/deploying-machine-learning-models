from my_module import square 

def test_square_gives_correct_output():
    # when
    subject = square(2)
    
    #then
    assert subject == 4