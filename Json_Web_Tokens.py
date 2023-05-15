JSON Web Tokens (JWTs) are a compact, URL-safe means of representing claims between two parties.
They are commonly used for authentication and authorization in web applications.
A JWT is a self-contained token that consists of three parts: a header, a payload, and a signature.
  Here's how JWTs work:

Header: The header of a JWT contains metadata about the type of token and the signing algorithm used.
  It typically consists of two parts: the token type (JWT) and the signing algorithm (e.g., HMAC SHA256 or RSA).
    The header is Base64Url encoded.

Payload: The payload contains the claims, which are statements about the user or additional data.
  Claims can be classified into three types: registered claims, public claims, and private claims.
    Registered claims are predefined and standardized, such as "iss" (issuer), "sub" (subject), "exp" (expiration time),
    and "aud" (audience). Public claims are defined by the application and can be publicly used or registered with an authority. 
    Private claims are specific to the application and are intended to be shared between parties that agree on their meaning.
    Like the header, the payload is also Base64Url encoded.

Signature: The signature is created by combining the encoded header, encoded payload, and a secret key known only to the server.
  The signature verifies the integrity of the token and ensures that it hasn't been tampered with.
  The specific signing algorithm defined in the header determines how the signature is generated.

Encoding and Delimiter: The three parts (header, payload, and signature) are concatenated with periods ('.') 
  as delimiters to form a complete JWT: header.payload.signature. The resulting JWT can be transmitted as a string through an HTTP header,
    a URL query parameter, or within the request body.

Token Generation: When a user successfully logs in or authenticates, the server generates a JWT for that user based on the provided claims.
  The server includes the JWT in the response to the client.

Token Verification: In subsequent requests, the client sends the JWT to the server,
  typically in the "Authorization" header with the "Bearer" scheme: Authorization: Bearer <token>. 
      The server receives the token and performs the following steps to verify it:

Extracts the header and payload from the JWT.
Computes the signature using the extracted header, payload, and the server's secret key.
Compares the computed signature with the received signature from the JWT.
Checks the token's expiration time and other validations defined by the server's authentication logic.
Token Usage: Once the server successfully verifies the JWT's signature and validates its claims,
  it treats the user associated with the token as authenticated. The user's identity and other information from the payload
  can be used to authorize access to protected resources or APIs.

JWTs are stateless, meaning the server does not need to store any session information. All the necessary information
is contained within the token itself. This makes JWTs scalable and suitable for distributed systems.

It's important to note that JWTs should be transmitted over a secure channel (HTTPS) to prevent 
interception and tampering of the token. Additionally, the server's secret key used for signing should be kept secure to maintain the integrity of the JWTs.































































































































































...
