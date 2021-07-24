# CON_TC_1014_REG, Sign-up with account already existing


def test_reg_1014():
    # getting sign-up form
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul/li[3]/a"))).click()
    time.sleep(5)
    user_registration("testella", "testella@gmail.com", "Teszt123")
    time.sleep(5)
    assert_handling("Registration failed!", "Email already taken.")


# CON_TC_1015_REG, Sign-up with not yet registered email but already existing username
# this test gives assertion error, app accepts multiple registration with same usernames/or not accepting valid email


def test_reg_1015():
    back_to_form()
    user_registration("testella", rnd_em, rnd_pw)
    time.sleep(5)
    assert_handling("Registration failed!", "Username already taken.")
