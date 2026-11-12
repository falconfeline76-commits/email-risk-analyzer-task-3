import re

urgent_pattern = r"\b(urgent|immediately|act now|within 24 hours|suspended|blocked)\b"
link_pattern = r"(https?://\S+|www\.\S+|click here|open this link)"
sensitive_pattern = r"\b(password|passcode|otp|one[- ]time password|verification code|bank details|card number|pin)\b"

email_text = input("Enter sample email text: ").strip()

if not email_text:
    print("Please enter some sample email text.")
else:
    risk_flags = []

    if re.search(urgent_pattern, email_text, re.IGNORECASE):
        risk_flags.append("Urgent or pressure language found.")

    if re.search(link_pattern, email_text, re.IGNORECASE):
        risk_flags.append("A link or click prompt was found; check it carefully.")

    if re.search(sensitive_pattern, email_text, re.IGNORECASE):
        risk_flags.append("The message mentions passwords, OTPs, or sensitive details.")

    if len(risk_flags) >= 3:
        risk_level = "HIGH"
    elif risk_flags:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    print(f"\nPossible email risk: {risk_level}")

    if risk_flags:
        for flag in risk_flags:
            print(f"- {flag}")
    else:
        print("No checked warning patterns were found.")

    print("\nThis is a simple keyword checker; it cannot prove an email is safe.")