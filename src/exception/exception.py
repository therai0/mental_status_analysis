import sys 


class CustomeException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        self.error_details = error_details

        _,_,exc_tb = self.error_details.exc_info()

        self.line_no = exc_tb.tb_lineno # where the error is 
        self.file_name = exc_tb.tb_frame.f_code.co_filename  # in which file error is showing


    def __str__(self):
        return f"Line no:{self.line_no}\n File name:{self.file_name}\n Error message:{self.error_message}"




