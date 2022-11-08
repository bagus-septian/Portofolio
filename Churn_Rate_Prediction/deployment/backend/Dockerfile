FROM tensorflow/serving

ENV MODEL_BASE_PATH /models
ENV MODEL_NAME churn_model

COPY model /models

COPY tf_serving_entypoint.sh /usr/bin/tf_serving_entypoint.sh
RUN chmod +x /usr/bin/tf_serving_entypoint.sh
ENTRYPOINT []
CMD ["/usr/bin/tf_serving_entypoint.sh"]