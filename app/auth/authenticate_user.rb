# app/auth/authenticate_user.rb
require 'securerandom'

class AuthenticateUser
    def initialize(email, password)
      @email = email
      @password = password
      @random_string = SecureRandom.urlsafe_base64(6)
    end
  
    # Service entry point
    def call
      JsonWebToken.encode( { user_id: user.id, user_random_string: user.random_string } ) if user
    end
  
    private
  
    attr_reader :email, :password, :random_string
  
    # verify user credentials
    def user
      user = User.find_by(email: email)
      if user  && user.authenticate(password)
        user.update(random_string: random_string)
        return user
      end
      # raise Authentication error if credentials are invalid
      raise(ExceptionHandler::AuthenticationError, Message.invalid_credentials)
    end
  end