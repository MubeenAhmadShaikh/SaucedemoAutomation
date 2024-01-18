# Use the official Python image as the base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set the working directory
WORKDIR /saucedemoapp

# Copy the entire project into the container
COPY . /saucedemoapp

# Copy the requirements file into the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Chrome and WebDriver
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

# Install Firefox and GeckoDriver
RUN apt-get update && apt-get install -y firefox-esr && \
    wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
    tar -xvzf geckodriver-v0.30.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver-v0.30.0-linux64.tar.gz && \
    apt-get clean


# Install OpenJDK (try default-jre)
RUN apt-get update && apt-get install -y default-jre


# Install Allure command line
RUN wget -O allure-commandline.zip https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.14.0/allure-commandline-2.14.0.zip \
    && unzip allure-commandline.zip -d /opt/ \
    && ln -s /opt/allure-2.14.0/bin/allure /usr/bin/allure \
    && rm allure-commandline.zip


#setting the allure path
ENV PATH="/opt/allure-2.14.0/bin:${PATH}"

# Set the Java home environment variable
ENV JAVA_HOME /usr/lib/jvm/default-java
ENV PATH $JAVA_HOME/bin:$PATH




RUN chmod -R +r /saucedemoapp/reports

# Create a directory to store reports
RUN mkdir -p /saucedemoapp/reports/saucedemo-report

WORKDIR /saucedemoapp/tests

# Define the CMD command
CMD ["sh", "-c", "if [ -n \"$TEST_FILE\" ]; then pytest $TEST_FILE -s -v ${MARKER_NAME:+-m $MARKER_NAME} --browser_name=$BROWSER_NAME --alluredir='/saucedemoapp/reports/allure-reports'; else pytest -s -v ${MARKER_NAME:+-m $MARKER_NAME} --browser_name=$BROWSER_NAME --alluredir='/saucedemoapp/reports/allure-reports'; fi ; allure generate '/saucedemoapp/reports/allure-reports' -o '/saucedemoapp/reports/generated-reports' ; allure-combine '/saucedemoapp/reports/generated-reports' --dest '/saucedemoapp/reports/saucedemo-report'"]

