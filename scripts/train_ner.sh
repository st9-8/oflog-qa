# Tokenization
java -cp ../../StanfordNER/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.process.PTBTokenizer ner_training.tsv > ner_training.tok

# Training
java -cp ../../StanfordNER/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop ner_training.prop

# Testing
# java -cp ../../StanfordNER/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../ner/ner-model.ser.gz -textFile sentences.txt > sentences_tagged.txt

# Testing with output tabbed
java -cp ../../StanfordNER/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../ner/ner-model.ser.gz -outputFormat tabbedEntities -textFile sentences.txt > sentences_tagged.tsv