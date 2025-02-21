from my_module import square 

def test_square_gives_correct_output(input_value):
    # when
    subject = square(input_value)
    
    #then
    assert subject == 16 