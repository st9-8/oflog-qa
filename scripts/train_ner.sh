# Tokenization
java -cp ../../StanfordNER/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.process.PTBTokenizer ner_training.tsv > ner_training.tok

# Training
java -cp ../../StanfordNER/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop ner_training.prop

# Testing
# java -cp ../../StanfordNER/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../ner/ner-model.ser.gz -textFile sentences.txt > sentences_tagged.txt

# Testing with output tabbed
java -cp ../../StanfordNER/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../ner/ner-model.ser.gz -outputFormat tabbedEntities -textFile sentences.txt > sentences_ner_tagged.tsv


# Training questions NER tagger
java -cp ../../StanfordNER/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop questions_ner_training.prop

# Testing questions NER tagger

java -cp ../../StanfordNER/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../ner/questions-ner-model.ser.gz -outputFormat tabbedEntities -textFile test_questions.txt > questions_ner_tagged.tsv


# Train CRF model
crfsuite learn -p c1=0.0 -p c2=1.0 -e2 -m oflog-qa.model ../data/CRF_training/qa_training.train.bnf

# Test CRF model

# ON Test data
crfsuite  tag -m oflog-qa.model -tpri ../data/CRF_training/qa_test.bnf

# ON Train data

crfsuite  tag -m oflog-qa.model -tpri ../data/CRF_training/qa_training.train.bnf